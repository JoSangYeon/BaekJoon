import java.io.*;
import java.util.*;

class Main
{
	public static void calc(int a, int b, int c, int cable, int[][] info)
	{
		int num=0;
		int cost=0;
		
		for(int i=0; i<cable; i++)
		{
			if(info[i][1] == 0)
			{
				if(a != 0) {a--; num++; cost += info[i][0];}
				else if(c != 0) {c--; num++; cost += info[i][0];}
			}
			else
			{
				if(b != 0) {b--; num++; cost += info[i][0];}
				else if(c != 0) {c--; num++; cost += info[i][0];}
			}
		}
		System.out.println(num+" "+cost);
	}
	public static void main(String[] args) throws Exception 
	{
		Scanner sc = new Scanner(System.in);
		
		int a,b,c;
		int cable;
		
		a = sc.nextInt();
		b = sc.nextInt();
		c = sc.nextInt();
		
		cable = sc.nextInt();
		int[][] info = new int[cable][2];
		for(int i=0; i<cable; i++)
		{
			int k = sc.nextInt();
			int t = sc.nextInt();
			
			info[i][0] = k;
			info[i][1] = t;
		}
		Arrays.sort(info, new Comparator<int[]>()
		{ @Override
			public int compare(int[] o1, int[] o2)
				{ return o1[0] - o2[0];}
		});
		
		//for(int i=0; i<cable; i++)
		//{System.out.println(info[i][0] + " " + info[i][1]);}
		
		calc(a,b,c,cable,info);
	}
}