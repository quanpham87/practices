using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Practices {
    class Program {
        static void Main(string[] args) {
            Q1(new int[] { });
            Q1(new int[] { 1,2,3,4,5 });
            Q1(new int[] { 3,2,2,1,2,2,1 });
        }

        /// <summary>
        /// 1. how many numbers?
        /// 2. how big is each value?
        /// 3. time complexity? i don't know how much time FirstOrDefault takes.
        /// 4. what if 2 elements have same # of appearances
        /// 
        /// THIS IS A VERY BAD SOLUTION
        /// can't calculate complexity
        /// at least O(n) for storing then some for filtering
        /// need to stop thinking .net way
        /// </summary>
        static void Q1(int[] values) {
            if (values.Length == 0) {
                Console.WriteLine("n/a");
                return;
            }

            var dict = new Dictionary<int, int>();
            foreach (var v in values) {
                if (dict.ContainsKey(v))
                    dict[v] += 1;
                else
                    dict.Add(v, 1);
            }

            var max = dict.FirstOrDefault(d => d.Value > values.Length / 2);
            Console.WriteLine(max.Key.ToString());
        }
    }
}
