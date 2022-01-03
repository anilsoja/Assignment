using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DelegateExample
{
    class Program
    {
        public delegate int calculator(int x, int y);

        static int Addition(int a, int b)
        {
            return a + b;
        }
        static int Subtraction(int a, int b)
        {
            return a - b;
        }
        static void Main(string[] args)
        {
            calculator c = new calculator(Program.Addition);
            Console.WriteLine("Addition of 5 and 10 is : {0}", c(10, 20));

            calculator d = new calculator(Program.Subtraction);
            Console.WriteLine("Subtraction of 5 and 10 is : {0}", d(5, 10));

            Console.ReadKey();
        }
    }
}
