using System.IO;
using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        
        var new_dict = new Dictionary<int, string>(){
            {1,"Apple"},{2,"Banana"}
        };
        new_dict.Add(3, "Grapes");
        new_dict.Add(4, "Orange");
       

        Console.WriteLine("Fruits:");
        foreach (var items in new_dict)

            Console.WriteLine("Key: {0} | Name: {1}", items.Key, items.Value);

    }
}
