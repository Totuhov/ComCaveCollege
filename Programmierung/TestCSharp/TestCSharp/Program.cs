using System;

namespace TestCSharp
{
    internal class Program
    {

        static void Tausch(ref int x, ref int y)
        {
            int c = x;
            y = x;
            x = c;
        }


        static void Main()
        {


            int i = 8;

            int j = 3;

            double d = i / j;



            Console.WriteLine(d);


        }        
    }
}
