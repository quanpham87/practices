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

            Q2(new int[] { 1, -3, 2, 5, -8 });

            Q7(new int[] { 2, 3, 1, 4, 2 }, 2);
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

        /// <summary>
        /// maximum sum of a continuous subsequence
        /// length of a subsequence? can a subsequence contains 1 element only?
        /// easiest way is 2 for loops, O(n^2)
        /// 
        /// based on the solution, the subsequence is sequential (i.e. only 1 move forward)
        /// bad description, or should it be a question for the interviewer?
        /// </summary>
        /// <param name="values"></param>
        static void Q2(int[] values) {
            if (values.Length == 1)
                Console.WriteLine(values[0]);
            if (values.Length == 0)
                Console.WriteLine(0);

            var max = values[0];
            for (var i = 0; i < values.Length; i++) {
                var current = values[i];
                for (var j = i + 1; j < values.Length - 1; j++) {
                    current += values[j];
                    max = Math.Max(current, max);
                }
            }

            Console.WriteLine(max);
        }

        /// <summary>
        /// binary tree questions, need to create binary tree class first
        /// </summary>
        static void Q3To6() { }

        /// <summary>
        /// design a class that you can add element and find the mean of the last N elements
        /// solution: 
        ///     a list<int> class
        ///     include a dictionary<int, int> where key = element count from last and value = mean of key elements
        ///     read: O(1)
        ///     write: O(n)
        /// </summary>
        /// <param name="values"></param>
        static void Q7(int[] values, int elementCount) {
            Console.WriteLine("--Q7--");
            var c = new Q7Class();
            foreach (var value in values)
                c.AddElement(value);

            Console.WriteLine(c.NElementMean[elementCount] / elementCount);
        }
    }

    public class Q7Class : List<int> {
        public Dictionary<int, int> NElementMean { get; set; }

        public void AddElement(int value) {
            this.Add(value);

            NElementMean.Add(NElementMean.Count + 1, 0);
            NElementMean[1] = value;

            for (var i = 2; i <= this.Count; i++)
                NElementMean[i] = this[this.Count - i] + NElementMean[i - 1];
        }

        public Q7Class() {
            NElementMean = new Dictionary<int, int>();
        }
    }
}
