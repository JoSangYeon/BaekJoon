import java.io.*;
import java.util.Scanner;

class Main
{
	public static void calc(int n, int m, int[] foods)
	{
		int myfood = 1;
		for(int i=0; i<m; i++)
		{
			int way = 0;
			
			way = Math.min(Math.abs(myfood-foods[i]), foods[i]+n-myfood);
			way = Math.min(way,myfood+n-foods[i]);
				
			System.out.print(way+" ");
			myfood = foods[i];
		}
		
	}
	public static void main(String[] args) throws Exception 
	{
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		
		int[] foods = new int[m];
		
		for(int i=0; i<m; i++) {foods[i] = sc.nextInt();}
		
		calc(n,m,foods);
	}
}