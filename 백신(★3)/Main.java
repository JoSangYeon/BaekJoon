import java.io.*;
import java.util.Scanner;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

class Node 
{
	int vertex;
	Node link;
	public Node(int v)
	{
		vertex = v;
		link = null;
	}
}

class Linked
{
	Node head;
	
	public Linked() {head = null;}
	boolean isEmpty() {return head == null;}
	void setHead(int v) {head= new Node(v);}
	
	void insert(int v)
	//insert Last의 형태의 insert Data 메소드이다. 
	{
		if(this.isEmpty()) {setHead(v); return;}
		else
		{
			Node temp = new Node(v);
			Node p = head;
			while(p.link != null)
				{p = p.link;}
			p.link = temp;
		}
	}
	
	public void print()
	{
		if(this.isEmpty()) {System.out.println("[ ]");}
		else
		{
			Node temp = head;
			System.out.print("[");
			while(temp.link != null)
			{
				System.out.print(temp.vertex+" ");
				temp = temp.link;
			}
			System.out.println(temp.vertex+"]");
		}
	}
}

class Graph
{	
	Linked[] heads;
	int n, m;
	int count;
	boolean[] visited;
	
	public Graph(int n, int m, int[][] arr) throws Exception
	{
		int a,b;
		this.n = n;
		this.m = m;
		
		heads = new Linked[n];
		for(int i=0; i<n; i++)
			{heads[i] = new Linked();}
		for(int i=0; i<m; i++)
		{
			a = arr[i][0];
			b = arr[i][1];
			
			heads[a-1].insert(b-1);
			heads[b-1].insert(a-1);
		}
		visited = new boolean[n];
		Arrays.fill(visited, false);
		count = 0;
	}
	
	public void setting() {Arrays.fill(visited, false); count = 0;}
	
	private int DFS(int v)
	{
		Node w; 
		visited[v] = true;
		this.count++;
		
		for(w=heads[v].head;w!=null; w=w.link)
		{
			if(!visited[w.vertex]) {DFS(w.vertex);}
		}
		return this.count;
	}
	
	public void calc()
	{
		int[][] result = new int[visited.length][2];
		for(int i=0; i<visited.length; i++)
		{
			this.DFS(i);
			result[i][0] = i+1;
			result[i][1] = this.count;
			
			this.setting();
		}
		
		int idx = 0;
		for(int i=1; i<result.length; i++)
		{
			if(result[idx][1] < result[i][1])
				{idx = i;}
		}
		
		System.out.println(result[idx][0] + " " + result[idx][1]);
	}
	
	public void displayGraph()
	{
		for(int i=0; i<heads.length; i++)
		{
			Linked temp = heads[i];
			System.out.print("vertex"+i+": ");
			temp.print();
		}
	}
}

class Main
{
	public static void main(String[] args) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int n, m, a, b;
		n = sc.nextInt();
		m = sc.nextInt();
		
		int[][] arr = new int[m][2];
		for(int i=0; i<m; i++)
		{
			a = sc.nextInt();
			b = sc.nextInt();
			
			arr[i][0] = a;
			arr[i][1] = b;
		}
		
		Graph g = new Graph(n,m,arr);
		g.calc();
		
	}
}