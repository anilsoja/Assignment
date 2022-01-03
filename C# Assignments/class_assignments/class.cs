using System.IO;
using System;

class Program
{
	static void Main()
	{
		Console.WriteLine("Enter the no: of students");
		string number = Console.ReadLine();
		int num = Convert.ToInt32(number);
		for (int i = 0; i < num; i++)
		{
			StudentReport student = new StudentReport();
			Console.WriteLine("Enter the name");
			string name = Console.ReadLine();
			student.details(name);
			Console.WriteLine("Enter the mark");
			string mark1 = Console.ReadLine();
			int num1 = Convert.ToInt32(mark1);
			string mark2 = Console.ReadLine();
			int num2 = Convert.ToInt32(mark2);
			string mark3 = Console.ReadLine();
			int num3 = Convert.ToInt32(mark3);
			string mark4 = Console.ReadLine();
			int num4 = Convert.ToInt32(mark4);
			string mark5 = Console.ReadLine();
			int num5 = Convert.ToInt32(mark5);

			student.marks(num1, num2, num3, num4, num5);
			Console.WriteLine("");
		}
	}
}
public class StudentReport
{
	int chemistry, physics, maths,hindi, english;
   string name;
	public void details(string s_name)
	{
		name = s_name;
		Console.WriteLine("Name : " + name);
	

	}
	public void grades(int x)
	{
		if (x >= 90)
		{
			Console.WriteLine(" Grade : A+");

		}
		else if (x >= 80)
		{
			Console.WriteLine(" Grade : A");
		}
		else if (x >= 70)
		{
			Console.WriteLine(" Grade : B+");
		}
		else if (x >= 60)
		{
			Console.WriteLine(" Grade : B");
		}
		else if (x >= 50)
		{
			Console.WriteLine(" Grade : C+");
		}
		else if (x >= 40)
		{
			Console.WriteLine(" Grade : C");
		}
		else if (x >= 30)
		{
			Console.WriteLine(" Grade : D");

		}
		else { Console.WriteLine("Grade : E"); }
	}
	public void mark_Detail(int x, int y, int z, int a, int b)
	{
		int marks = x + y + z + a + b;
		Console.WriteLine("Total mark: " + marks);
		int avg = marks / 5;
		Console.Write("Total ");
		grades(avg);
	}
	public void marks(int m, int c, int e, int p, int h)
	{
		chemistry = c;
		physics = p;
		maths = m;
		hindi = h;
		english = e;
		Console.Write("Chemistry : " + chemistry);
		grades(chemistry);
		Console.Write("Physics : " + physics);
		grades(physics);
		Console.Write("Maths : " + maths);
		grades(maths);
		Console.Write("Biology : " + hindi);
		grades(hindi);
		Console.Write("English : " + english);
		grades(english);
	 mark_Detail(chemistry, physics, maths, hindi, english);
	}
}
