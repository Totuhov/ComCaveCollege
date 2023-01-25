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
            int a = 1, b = 2;

            Tausch(ref a, ref b);
        }

        
    }
}
