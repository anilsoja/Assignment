using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AssignmentConsoleApp1
{
    internal class Program
    {
        static void Main(string[] args)
        {  
            SortedList < int, string > Collections = new SortedList < int, string > ();  
         
            Collections.Add(2, "Bat");  
            Collections.Add(6, "Fan");
            Collections.Add(3, "Cat");  
            Collections.Add(7, "Gorilla");  
            
            Console.WriteLine("Before adding items are:");  
            foreach(KeyValuePair < int, string > pair in Collections) 
            {  
                Console.WriteLine("{0} : {1}", pair.Key, pair.Value);  
            }  

            Collections.Add(4, "Dog");
            Collections.Add(1, "Apple");   
            Collections.Add(5, "Elephant");

            Console.WriteLine("\nAfter adding items are:");  
            foreach(KeyValuePair < int, string > pair in Collections) 
            {  
                Console.WriteLine("{0} : {1}", pair.Key, pair.Value);  
            }
        }
    }
}
