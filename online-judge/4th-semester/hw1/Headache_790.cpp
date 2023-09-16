using namespace std;

#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <sstream>
#include <algorithm>

class Submission
{
    public:
        int id;
        char letter;
        int time;
        char status;
        Submission(int i, char l, int t, char s)
        {
            id = i;
            letter = l;
            time = t;
            status = s;
        } 
};

class Team
{
    public:
        //problem letter = [time, solved (0,1)]
        map<char, vector<int>> sub;
        int solved;
        int id;
        int time;

        Team()
        {
            solved = 0;
            time = 0;
            sub['A'] = vector<int>(2,0);
            sub['B'] = vector<int>(2,0);
            sub['C'] = vector<int>(2,0);
            sub['D'] = vector<int>(2,0);
            sub['E'] = vector<int>(2,0);
            sub['F'] = vector<int>(2,0);
            sub['G'] = vector<int>(2,0);
        }
};

void clearArray(Team arr[])
{
    for(int i = 0; i < 25; i++)
    {
        arr[i].id = i + 1;
        arr[i].solved = 0;
        arr[i].time = 0;
        for(map<char, vector<int>>::iterator it = arr[i].sub.begin(); it != arr[i].sub.end(); it++)
        {
            it->second[0] = 0;
            it->second[1] = 0;
        }
    }
}

bool comp(Team self, Team other)
{
    if(self.solved == 0 && other.solved == 0)
    {
        return self.id < other.id;
    }
    else if(self.solved == other.solved)
    {
        if(self.time == other.time)
        {
            return self.id < other.id;
        }
        return self.time < other.time;
    }
    else
    {
        return self.solved > other.solved;
    }
}

bool compS(Submission self, Submission other)
{
    if(self.time != other.time)
    {
        return self.time < other.time;
    }
    return self.status < other.status;
}

int main()
{
    bool flag;
    vector<Submission> subList;
    int maxNumb = 0, rank = 0, lastTime = 0, lastSolved = 0;
    Team teamArr[25];
    clearArray(teamArr);
    string line, sc;
    char letter, status;
    int cases;
    int teamId = 0, minutes = 0, hours = 0;
    getline(cin, sc);
    stringstream(sc) >> cases;
    cin.ignore(1, '\n');
    while(cases--)
    {

        getline(cin, line);
        while(line != "\n" and line != "" and line != "stop")
        {
            stringstream split(line);
            split >> teamId;
            split >> letter;
            split >> hours;
            split.ignore(1, ':');
            split >> minutes;
            split >> status;
            minutes += hours * 60;
            
            subList.push_back(Submission(teamId, letter, minutes, status));

            getline(cin, line);
        }

        sort(subList.begin(), subList.end(), compS);

        for(int j = 0; j < subList.size(); j++)
        {
            teamId = subList[j].id;
            letter = subList[j].letter;
            minutes = subList[j].time;
            status = subList[j].status;
            if(teamId > maxNumb)
            {
                maxNumb = teamId;
            }
            if(teamArr[teamId - 1].sub[letter][1] == 0)
            {
                if(status == 'N')
                {
                    teamArr[teamId - 1].sub[letter][0] += 20;
                }
                else
                {
                    teamArr[teamId - 1].sub[letter][1] = 1;
                    teamArr[teamId - 1].solved += 1;
                    teamArr[teamId - 1].sub[letter][0] += minutes;
                    teamArr[teamId - 1].time += teamArr[teamId - 1].sub[letter][0];
                }
            }
        }

        sort(begin(teamArr), end(teamArr), comp);

        cout << "RANK TEAM PRO/SOLVED TIME" << endl;
        rank = 1;
        lastTime = teamArr[0].time;
        lastSolved = teamArr[0].solved;
        flag = false;
        for(int i = 0; i < maxNumb; i++)
        {
            if(i != 0 && teamArr[i].solved != lastSolved)
            {
                if(flag)
                {
                    rank = i + 1;
                    flag = false;
                }
				else
				{
					rank++;
				}
                lastSolved = teamArr[i].solved;
                lastTime = teamArr[i].time;
            }
            else if(i != 0 && teamArr[i].solved == lastSolved)
            {
                if(teamArr[i].time != lastTime)
                {
					if(flag)
					{
						rank = i + 1;
						flag = false;
					}
					else
					{
						rank++;
					}
                    lastTime = teamArr[i].time;
                }
                else
                {
                    flag = true;
                }
            }
            printf("%4d %4d", rank, teamArr[i].id);
            if(teamArr[i].solved != 0)
            {
                printf("%5d %10d", teamArr[i].solved, teamArr[i].time);
            }
            printf("\n");
        }
		if(cases != 0)
		{
			printf("\n");
		}
        clearArray(teamArr);
        maxNumb = 0;
        subList.clear();
    }
    
    return 0;
}