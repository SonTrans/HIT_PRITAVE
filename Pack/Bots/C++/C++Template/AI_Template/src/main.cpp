#include <ai/Game.h>
#include <ai/AI.h>
#include <time.h>
#include <vector>
#include <algorithm>
#include <cmath>
#include <queue>
#include <map>
#ifdef _WIN32
#include <winsock2.h>
#include <windows.h>
#endif
#define NOMINMAX
// ==================== HOW TO RUN THIS =====================
// Call:
// "AI_Template.exe -h [host] -p [port] -k [key]"
//
// If no argument given, it'll be 127.0.0.1:3011
// key is a secret string that authenticate the bot identity
// it is not required when testing
// ===========================================================

//////////////////////////////////////////////////////////////////////////////////////
//                                                                                  //
//                                    GAME RULES                                    //
//                                                                                  //
//////////////////////////////////////////////////////////////////////////////////////
// - The game is played on a map of 20x20 blocks where [x,y] is referred as the     //
// block at column x and row y.                                                     //
// - Each team has 1 main base, 2 side bases and 4 tanks.                           //
// - At the beginning of a game, each player will choose 4 tanks and place them     //
// on the map (not on any bases/obstacles/tanks).                                   //
// - The game is played in real-time mode. Each player will control 4 tanks in      //
// order to defend their bases and at the same time, try to destroy their enemy’s   //
// bases.                                                                           //
// -Your tank bullets or cannon shells will pass other allied tank (not friendly    //
// fire), but will damage your own bases, so watch where you firing.                //
// -A destroyed tank will allow bullet to pass through it, but still not allow      //
// other tanks to pass through.                                                     //
// - When the game starts (and after each 30 seconds) , a random power-up will be   //
// spawn at 1 of 3 bridges (if there are still space) at location:                  //
// [10.5, 1.5], [10.5, 10.5], [10.5, 19.5].                                         //
// - Power-ups are friendly-fired and have area of effect (AOE) damage. All units   //
// near the struck location will be affected. Use them wisely.                      //
// - The game is over when:                                                         //
//   + The main base of 1 team is destroyed. The other team is the winner.          //
//   + If all tanks of a team are destroyed, the other team is the winner.          //
//   + After 120 seconds, if both main bases are not destroyed, the team with more  //
//   side bases remaining is the winner.                                            //
//   + If both team have the same bases remaining, the game will change to “Sudden  //
//   Death” mode. In Sudden Death mode:                                             //
//     * 2 teams will play for extra 30 seconds.                                    //
//     * All destructible obstacles are removed.                                    //
//     * If 1 team can destroy any base, they are the winner.                       //
//     * After Sudden Death mode is over, the team has more tanks remaining is the  //
//     winner.                                                                      //
//   + The time is over. If it’s an active game (i.e. Some tanks and/or bases are   // 
//   destroyed), the result is a DRAW. If nothing is destroyed, it’s a BAD_DRAW.    //
//                                                                                  //
// Please read the detailed rule on our web site at:                                //
//   http://han-ai-contest2016.gameloft.com                                         //
//////////////////////////////////////////////////////////////////////////////////////

// This function is called automatically to set your tanks on the map
// Arrange your tanks as you wish using PlaceTank() command
// You can only place NUMBER_OF_TANK tanks in the map
// IMPORTANT: Remember to place all your tanks and the coordinates must be integers.
struct Point {
    int x, y;
    bool operator==(const Point& other) const { return x == other.x && y == other.y; }
    bool operator!=(const Point& other) const { return x != other.x || y != other.y; }
    bool operator<(const Point& other) const {
        if (x != other.x) return x < other.x;
        return y < other.y;
    }
};

bool ktratankcan(int x, int y) {
    AI* p = AI::GetInstance();

    for (int i = 0; i < NUMBER_OF_TANK; i++) {
        Tank* t = p->GetEnemyTank(i);
        if (t) {
            int tx = (int)(t->GetX() + 0.5f);
            int ty = (int)(t->GetY() + 0.5f);
            if (tx == x && ty == y) {
                if (t->GetHP() <= 0) return true;        
                if (t->GetType() == TANK_HEAVY) return true; 
               
            }
        }
    }

    for (int i = 0; i < NUMBER_OF_TANK; i++) {
        Tank* t = p->GetMyTank(i);
        if (t) {
            int tx = (int)(t->GetX() + 0.5f);
            int ty = (int)(t->GetY() + 0.5f);
            if (tx == x && ty == y) {
                if (t->GetHP() <= 0) return true;      
                if (t->GetType() == TANK_HEAVY) return true; 
 
            }
        }
    }
    return false; 
}

std::vector<Point> basedich(int myTeam) {
    std::vector<Point> blocks;
    if (myTeam == TEAM_1) {
        blocks.push_back({ 19, 10 }); blocks.push_back({ 19, 11 });
        blocks.push_back({ 20, 10 }); blocks.push_back({ 20, 11 });
    }
    else {
        blocks.push_back({ 1, 10 }); blocks.push_back({ 1, 11 });
        blocks.push_back({ 2, 10 }); blocks.push_back({ 2, 11 });
    }
    return blocks;
}

Point xddich(int team, int tankID) {
    AI* p = AI::GetInstance();
    Tank* myTank = p->GetMyTank(tankID);
    if (!myTank) return { 10, 10 };

    int ix = (int)(myTank->GetX() + 0.5f);
    int iy = (int)(myTank->GetY() + 0.5f);

    if (team == TEAM_1) {
        bool borderBlocked = ktratankcan(13, 20) || ktratankcan(14, 20);

        if (borderBlocked) {
            if (ix < 12) return { 12, 15 };
            if (ix >= 12 && ix < 16) {
                return { 16, 15 };
            }
            if (ix >= 16 && iy < 20 && ix < 19) return { 19, 20 };
        }

        switch (tankID) {
        case 0: return { 20, 17 };
        case 1: return { 20, 18 };
        case 2: return { 20, 19 };
        case 3: return { 20, 20 };
        }
    }
    else {
        switch (tankID) {
        case 0: return { 1, 4 };
        case 1: return { 1, 3 };
        case 2: return { 1, 2 };
        case 3: return { 1, 1 };
        }
    }
    return { 10, 10 };
}


bool ktradichuyen(int x, int y) {
    AI* p = AI::GetInstance();
    if (x < 1 || x > 20 || y < 1 || y > 20) return false;
    int block = p->GetBlock(x, y);
    if (block == BLOCK_HARD_OBSTACLE || block == BLOCK_SOFT_OBSTACLE || block == BLOCK_WATER) return false;

    auto myBases = p->GetMyBases();
    auto enemyBases = p->GetEnemyBases();
    for (auto b : myBases) if ((int)b->GetX() == x && (int)b->GetY() == y) return false;
    for (auto b : enemyBases) if ((int)b->GetX() == x && (int)b->GetY() == y) return false;
    if (ktratankcan(x, y)) return false;

    return true;
}

bool checksight(float x1, float y1, float x2, float y2) {
    AI* p = AI::GetInstance();
    if (std::abs(x1 - x2) > 0.6f && std::abs(y1 - y2) > 0.6f) return false;

    int start, end, fixed;
    bool horizontal = (std::abs(y1 - y2) < 0.6f);

    if (horizontal) {
        start = (int)min(x1, x2); end = (int)max(x1, x2); fixed = (int)(y1 + 0.5f);
        for (int x = start + 1; x < end; x++) {
            if (p->GetBlock(x, fixed) == BLOCK_HARD_OBSTACLE) return false;
        }
    }
    else {
        start = (int)min(y1, y2); end = (int)max(y1, y2); fixed = (int)(x1 + 0.5f);
        for (int y = start + 1; y < end; y++) {
            if (p->GetBlock(fixed, y) == BLOCK_HARD_OBSTACLE) return false;
        }
    }
    return true;
}

int tinhkhoangcach(Point a, Point b) { return std::abs(a.x - b.x) + std::abs(a.y - b.y); }

int Asao(int sx, int sy, int ex, int ey) {
    if (sx == ex && sy == ey) return 0;
    typedef std::pair<int, Point> PQElement;
    std::priority_queue<PQElement, std::vector<PQElement>, std::greater<PQElement>> pq;
    Point start = { sx, sy }; Point goal = { ex, ey };
    std::map<Point, Point> cameFrom; std::map<Point, int> costSoFar;

    pq.push({ 0, start }); cameFrom[start] = start; costSoFar[start] = 0;
    bool found = false;
    int dx[] = { 0, 0, -1, 1 }; int dy[] = { -1, 1, 0, 0 };
    int dirs[] = { DIRECTION_UP, DIRECTION_DOWN, DIRECTION_LEFT, DIRECTION_RIGHT };

    while (!pq.empty()) {
        Point current = pq.top().second; pq.pop();
        if (current == goal) { found = true; break; }
        if (costSoFar[current] > 200) continue;

        for (int i = 0; i < 4; i++) {
            Point next = { current.x + dx[i], current.y + dy[i] };
            if (ktradichuyen(next.x, next.y)) {
                int newCost = costSoFar[current] + 1;
                if (costSoFar.find(next) == costSoFar.end() || newCost < costSoFar[next]) {
                    costSoFar[next] = newCost;
                    int priority = newCost + tinhkhoangcach(next, goal);
                    pq.push({ priority, next });
                    cameFrom[next] = current;
                }
            }
        }
    }
    if (!found) { 
        if (sx < ex && ktradichuyen(sx + 1, sy)) return DIRECTION_RIGHT;
        if (sx > ex && ktradichuyen(sx - 1, sy)) return DIRECTION_LEFT;
        if (sy < ey && ktradichuyen(sx, sy + 1)) return DIRECTION_DOWN;
        if (sy > ey && ktradichuyen(sx, sy - 1)) return DIRECTION_UP;
        return 0;
    }
    Point curr = goal;
    if (cameFrom.find(curr) == cameFrom.end()) {
        int minH = 9999; Point bestNear = start;
        for (std::map<Point, Point>::iterator it = cameFrom.begin(); it != cameFrom.end(); ++it) {
            if (tinhkhoangcach(it->first, goal) < minH) { minH = tinhkhoangcach(it->first, goal); bestNear = it->first; }
        }
        curr = bestNear;
    }
    while (cameFrom[curr] != start && curr != start) curr = cameFrom[curr];
    if (curr.x > sx) return DIRECTION_RIGHT;
    if (curr.x < sx) return DIRECTION_LEFT;
    if (curr.y > sy) return DIRECTION_DOWN;
    if (curr.y < sy) return DIRECTION_UP;
    return 0;
}

int dichuyen(float currentX, float currentY, int nextDir) {
    float threshold = 0.15f;
    int ix = (int)(currentX + 0.5f); int iy = (int)(currentY + 0.5f);
    float diffX = currentX - ix; float diffY = currentY - iy;
    if (nextDir == 0) {
        if (diffX > threshold) return DIRECTION_LEFT; if (diffX < -threshold) return DIRECTION_RIGHT;
        if (diffY > threshold) return DIRECTION_UP; if (diffY < -threshold) return DIRECTION_DOWN;
        return 0;
    }
    if (nextDir == DIRECTION_UP || nextDir == DIRECTION_DOWN) {
        if (diffX > threshold) return DIRECTION_LEFT; if (diffX < -threshold) return DIRECTION_RIGHT;
    }
    if (nextDir == DIRECTION_LEFT || nextDir == DIRECTION_RIGHT) {
        if (diffY > threshold) return DIRECTION_UP; if (diffY < -threshold) return DIRECTION_DOWN;
    }
    return nextDir;
}



void chienthuat(Tank* myTank) {
    if (!myTank || myTank->GetHP() <= 0) return;
    AI* p = AI::GetInstance();
    int id = myTank->GetID();
    int team = p->GetMyTeam();
    float fx = myTank->GetX(); float fy = myTank->GetY();
    int ix = (int)(fx + 0.5f); int iy = (int)(fy + 0.5f);

    Point target = xddich(team, id);

    std::vector<Point> baseBlocks = basedich(team);
    bool shouldShoot = false;
    Point shootTarget = { -1, -1 };

    for (Point b : baseBlocks) {
        if (checksight(fx, fy, (float)b.x, (float)b.y)) { shouldShoot = true; shootTarget = b; break; }
    }
    if (!shouldShoot) {
        for (int i = 0; i < NUMBER_OF_TANK; i++) {
            Tank* en = p->GetEnemyTank(i);
            if (en && en->GetHP() > 0 && checksight(fx, fy, en->GetX(), en->GetY())) { shouldShoot = true; break; }
        }
        if (!shouldShoot) {
            auto bases = p->GetEnemyBases();
            for (auto b : bases) if (b->GetHP() > 0 && checksight(fx, fy, b->GetX(), b->GetY())) { shouldShoot = true; break; }
        }
    }

    int moveDir = 0;
    bool forceStop = false;

    bool inSniperLane = (team == TEAM_1) ? (fx >= 19.5f) : (fx <= 1.5f);

    if (inSniperLane) {

        float targetX = (float)target.x;
        float diffX = targetX - fx;

        if (std::abs(diffX) > 0.15f) { 
            int intendedDir = (diffX > 0) ? DIRECTION_RIGHT : DIRECTION_LEFT;
            moveDir = dichuyen(fx, fy, intendedDir);
        }
        else {
            float targetY = (float)target.y;
            float diffY = targetY - fy;

            if (std::abs(diffY) > 0.2f) { 
                int intendedDir = (diffY > 0) ? DIRECTION_DOWN : DIRECTION_UP;
                moveDir = dichuyen(fx, fy, intendedDir);
            }
            else {
                forceStop = true;
            }
        }

        if (forceStop) {
            if (shootTarget.x != -1) {
                float dx = (float)shootTarget.x - fx; float dy = (float)shootTarget.y - fy;
                if (std::abs(dx) > std::abs(dy)) moveDir = (dx > 0) ? DIRECTION_RIGHT : DIRECTION_LEFT;
                else moveDir = (dy > 0) ? DIRECTION_DOWN : DIRECTION_UP;
                shouldShoot = true;
            }
            else moveDir = (team == TEAM_1) ? DIRECTION_LEFT : DIRECTION_RIGHT;
        }
    }
    else {
        int roughDir = Asao(ix, iy, target.x, target.y);
        moveDir = dichuyen(fx, fy, roughDir);
    }

    Game::CommandTank(id, moveDir, !forceStop, shouldShoot);
}
void AI_Placement() {
    AI* p_AI = AI::GetInstance();
    if (p_AI->GetMyTeam() == TEAM_1) {
        Game::PlaceTank(TANK_MEDIUM, 7, 20);
        Game::PlaceTank(TANK_MEDIUM, 6, 20);
        Game::PlaceTank(TANK_MEDIUM, 5, 20);
        Game::PlaceTank(TANK_MEDIUM, 4, 20);
    }
    else {
        Game::PlaceTank(TANK_LIGHT, 14, 1);
        Game::PlaceTank(TANK_LIGHT, 15, 1);
        Game::PlaceTank(TANK_LIGHT, 16, 1);
        Game::PlaceTank(TANK_LIGHT, 17, 1);
    }
}

void AI_Update() {
    AI* p_AI = AI::GetInstance();
    for (int i = 0; i < NUMBER_OF_TANK; i++) chienthuat(p_AI->GetMyTank(i));
    Base* mainBase = nullptr;
    auto bases = p_AI->GetEnemyBases();
    for (auto b : bases) if (b->GetType() == BASE_MAIN) mainBase = b;
    if (mainBase) {
        if (p_AI->HasAirstrike()) p_AI->UseAirstrike(mainBase->GetX(), mainBase->GetY());
        if (p_AI->HasEMP()) p_AI->UseEMP(mainBase->GetX(), mainBase->GetY());
    }
    Game::GetInstance()->SendCommand();
}

////////////////////////////////////////////////////////////
//                DON'T TOUCH THIS PART                   //
////////////////////////////////////////////////////////////

int main(int argc, char* argv[])
{
    srand(clock());

#ifdef _WIN32
    INT rc;
    WSADATA wsaData;

    rc = WSAStartup(MAKEWORD(2, 2), &wsaData);
    if (rc) {
        printf("WSAStartup Failed.\n");
        return 1;
    }
#endif

    Game::CreateInstance();
    Game* p_Game = Game::GetInstance();

    // Create connection
    if (p_Game->Connect(argc, argv) == -1)
    {
        LOG("Failed to connect to server!\n");
        return -1;
    }

    // Set up function pointers
    AI::GetInstance()->PlaceTank = &AI_Placement;
    AI::GetInstance()->Update = &AI_Update;

    // Polling every 100ms until the connection is dead
    p_Game->PollingFromServer();

    Game::DestroyInstance();

#ifdef _WIN32
    WSACleanup();
#endif
    return 0;
}