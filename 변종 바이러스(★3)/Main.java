import java.io.*;
import java.util.Scanner;

class UnionFind
{
	int[] list;
	int[] li;
	int[][] board;
	int n;
	int m;
	int nn;
	
	public UnionFind(int n, int m)
	{
		this.n = n;
		this.m = m;
		nn = n+2;
		list = new int[nn*nn];
		li = new int[nn*nn];
		board = new int[n][n];
		
		for(int y=0; y<nn; y++)
		{
			for(int x=0; x<nn; x++)
			{
				if(!check(x,y)) {list[point(x,y)] = -1;}
				else {list[point(x,y)] = point(x,y);}
				li[point(x,y)] = 1;
			}
		}
	}
	
	public boolean check(int x, int y) {return 0<x && x<nn-1 && 0<y && y<nn-1;}
	public int point(int x, int y) {return x+nn*y;}
	
	public void print()
	{
		for(int i=0; i<nn*nn; i++)
		{
			if(i%nn==0) {System.out.println();}
			System.out.print(list[i]+"\t");
		}
	}
	
	public int find(int point)
	{
		if(list[point] == point) {return point;}
		else {return find(list[point]);}
	}
	
	public int union(int p1, int p2)
	{
		int i = find(p1);
		int j = find(p2);
		
		if(i != j)
		{
			list[j] = i;
			li[j] = li[i] += li[j];
		}
		return li[i];
	}
	
	public int count(int p)
	{
		int count = 0;
		for(int i=0; i<list.length; i++)
		{
			if(list[i] == p) {count++;}
		}
		return count;
	}
}

class Main
{
	public static void main(String[] args) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		int[] Xdir = {1,-1,0,0};
		int[] Ydir = {0,0,-1,1};
		
		UnionFind ans = new UnionFind(n,m);
		
		for(int i=0; i<m; i++)
		{
			int x = sc.nextInt();
			int y = sc.nextInt();
			
			ans.board[x-1][y-1] = 1;
			
			for(int j=0; j<4; j++)
			{
				int dx = x+Xdir[j];
				int dy = y+Ydir[j];
				int dp = ans.point(dx, dy);
				int p = ans.point(x, y);
				if(ans.check(dx, dy) && ans.board[dx-1][dy-1] == 1)
				{
					ans.union(p, dp);
				}
			}
			//ans.print();
			System.out.println(ans.li[ans.point(x, y)]);
		}
	}
}