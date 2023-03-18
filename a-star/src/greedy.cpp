#include <iostream>
#include <map>
#include <vector>
#include <limits>

#define MAX_NODES_NUM 26

using namespace std;

vector<char> findMinPath(map<char, vector<pair<char, double>>> graph, char source, char dest){
    char cur = source;
    bool visited[MAX_NODES_NUM] = {false};
    visited[cur - 'a'] = true;
    vector<char> res;
    res.push_back(source);

    while (cur != dest){
        double min = numeric_limits<double>::max();
        char next;
        bool flag = false;

        for (auto &n: graph[cur])
            if (!visited[n.first - 'a'] && n.second < min){
                min = n.second;
                next = n.first;
                flag = true;
            }

        visited[cur - 'a'] = true;

        if (!flag){
            if (!res.empty()){
                res.pop_back();
                cur = res.back();
            }
            continue;
        }

        cur = next;
        res.push_back(cur);
    }

    return res;
}

int main(){
    double weight;
    map<char, vector<pair<char, double>>> graph;

    char source, dest, e_start, e_end;
    cin >> source >> dest;

    while (cin >> e_start >> e_end >> weight) {
        graph[e_start].push_back({e_end, weight});
        if (cin.eof()) break;
    }

    vector<char> res = findMinPath(graph, source, dest);
    for (auto s: res)
        cout << s;
    return 0;
}