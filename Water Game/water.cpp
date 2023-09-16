#include <bits/stdc++.h>
using namespace std;

bool isComplete(vector<int>&bottle){
    unordered_set<int> s(bottle.begin(), bottle.end());
    return s.size()==0 || s.size()==1 && bottle.size()==4;
}

bool isValid(vector<vector<int>>&bottles){
    for(auto&bottle:bottles){
        if(!isComplete(bottle)) return false;
    }
    return true;
}

// can pour from i to j
bool canPour(vector<int>& bottleI, vector<int>&bottleJ){
    if(bottleI.empty()) return false;
    int capacity = 4-bottleJ.size();
    int numBack = 0;
    for(int i= bottleI.size()-1; i>=0; i--){
        if(bottleI[i]==bottleI.back()) numBack++;
        else break;
    }
    if(bottleJ.empty()) return numBack != bottleI.size();
    else {
        return numBack <= capacity && bottleJ.back() == bottleI.back();
    }
}

void printBottles(vector<vector<int>>&bottles) {
    cout << "Bottles:~~~\n";
    for(auto&bottle:bottles){
        for(auto&x:bottle) cout << x << ' '; cout << '\n';
    }
    cout << "~~~\n";
}

set<vector<vector<int>>> vis;
vector<pair<int,int>> actions;

bool solve(vector<vector<int>>&bottles){
    vis.insert(bottles);
    if(isValid(bottles)) {
        cout << actions.size() << '\n';
        for(auto&[startBottle,endBottle]:actions){
            cout << startBottle << "->" << endBottle << '\n';
        }
        return true;
    }

    for(int i=0; i<bottles.size(); i++){
        if(isComplete(bottles[i])) continue;
        for(int j=0; j<bottles.size(); j++){
            if(i==j) continue;
            if(!canPour(bottles[i], bottles[j])) continue;
            actions.push_back({i,j});
            vector<vector<int>> prevState = bottles;
            while(bottles[j].size()<4 && bottles[i].size() && (bottles[j].empty() || bottles[i].back() == bottles[j].back())){
                bottles[j].push_back(bottles[i].back());
                bottles[i].pop_back();
            }
            if(!vis.count(bottles)){
                if(solve(bottles)) return true;
            }
            actions.pop_back();
            bottles = prevState;
        }
    }
    return false;
}


int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    vector<vector<int>> bottles105
    {
        {4,3,2,1},
        {8,7,6,5},
        {10,10,9,8},
        {8,10,5,11},
        {9,4,9,6},
        {8,6,3,9},
        {5,11,12,2},
        {7,12,2,7},
        {11,5,6,4},
        {1,12,10,11},
        {1,3,12,1},
        {7,3,2,4},
        {},
        {}
    };

    vector<vector<int>> bottles108
    {
        {3,2,1,1},
        {6,4,5,4},
        {6,1,2,7},
        {8,2,3,4},
        {3,5,1,9},
        {8,3,5,6},
        {7,8,6,9},
        {9,2,7,7},
        {5,4,9,8},
        {},
        {}
    };

    if(solve(bottles108)) cout << "SOLVED\n";
    else cout << "FAILED\n";
}
