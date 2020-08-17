import java.io.*;
import java.util.Scanner;

class UF
{
	int[] people;
	int[] size;
	
	public UF(int n)
	{
		people = new int[n+1];
		size = new int[n+1];
		for(int i=0; i<n+1; i++)
		{
			people[i] = i;
			size[i] = 1;
		}
	}
	
	public int find(int x)
	{
		if(people[x] == x) {return x;}
		else {return people[x] = find(people[x]);}
	}
	
	public void union(int x, int y)
	{
		x = find(x);
		y = find(y);
		if(x != y)
		{
			people[y] = x;
			size[x] += size[y];
			size[y] = size[x];
		}
	}
}

class Main
{
	public static void main(String[] args) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int n,m;
		
		n = sc.nextInt();
		m = sc.nextInt();
		
		UF uf = new UF(n);
		
		for(int i=0; i<m; i++)
		{
			int num = sc.nextInt();
			int p = 0;
			for(int k=0; k<num; k++)
			{
				int temp = sc.nextInt();
				if(p != 0)
				{uf.union(p,temp);}
				p = temp;
			}
		}
		for(int i=1; i<n+1; i++)
		{
			System.out.print(uf.size[uf.find(i)]+" ");
		}
	}
}