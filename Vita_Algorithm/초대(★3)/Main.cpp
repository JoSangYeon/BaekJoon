#include <iostream>
#include <vector>
using namespace std;

int result;

void calc(int s, int pick, int stat, vector<int> datas)
{
	if(pick == 0)
	{
		stat = ~stat;
		int count = 0;
		for(int i=0; i<datas.size(); i++)
		{
			if((stat&datas[i])==0) {count++;}
		}
		result = max(result, count);
		return;
	}
	
	for(int i=2; i<10; i++)
	{
		if(stat & 1<<i) {continue;}
		
		calc(s+1, pick-1, stat|(1<<i), datas);
	}
}

int main()
{
	int n,k;
	vector<int> datas;
	cin >> n >> k;
	
	for(int i=0; i<n; i++)
	{
		int s = 1;
		int num;
		cin >> num;
		while(num != 0)
		{
			s |= (1 << (num % 10));
			num /= 10;
		}
		datas.push_back(s);
	}
	
	calc(0, k-2, 3, datas);
	cout << result;
}