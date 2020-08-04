import java.io.*;
import java.util.Scanner;

class Main
{
	public static void calc(int n, int money, int[] data)
	{
		int GCoin=0;
		int total=0;
		int min, max;
		
		min=0;
		for(int i=0; i<n; i++)
			{if(data[min] > data[i]) {min = i;}}
		max = min;
		for(int i=min; i<n; i++)
		{
			if(data[max] < data[i]) {max = i;}
		}
		
		GCoin = money/data[min];
		money = money%data[min];
		
		total = money+(GCoin*data[max]);
		
		System.out.println(total);
	}
	public static void main(String[] args) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int money = sc.nextInt();
		
		int[] data = new int[n];
		
		for(int i=0; i<n; i++) {data[i] = sc.nextInt();}

		
		calc(n,money,data);
	}
}