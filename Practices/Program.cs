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

            Q8(new List<Tuple<int, int>>() { 
                new Tuple<int,int>(1,3),
                new Tuple<int,int>(5,10),
                new Tuple<int,int>(9,31),
                new Tuple<int,int>(12,30)
            });

            Q9(new List<int>() { 2, 4, 5, 7, 8 }, 4);
            Q9(new List<int>() { 2, 4, 5, 7, 8 }, 9);
            Q10(new List<int>() { 9, 7, 2, 8, 5, 6, 3, 4 });
            Q11(new List<int>() { 1, 2, 3, 4, 5, 4, 3, 2 });
            Q11LogN(new List<int>() { 1, 2, 3, 4, 5, 4, 3, 2 });
        }

        static void WL(object str) {
            Console.WriteLine(str);
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
                WL("n/a");
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
            WL(max.Key.ToString());
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
                WL(values[0]);
            if (values.Length == 0)
                WL(0);

            var max = values[0];
            for (var i = 0; i < values.Length; i++) {
                var current = values[i];
                for (var j = i + 1; j < values.Length - 1; j++) {
                    current += values[j];
                    max = Math.Max(current, max);
                }
            }

            WL(max);
        }

        /// <summary>
        /// binary tree questions, need to create binary tree class first
        /// </summary>
        static void Q3To6() { }

        /// <summary>
        /// given 2 trees, determine if they're the same
        /// </summary>
        static void Q3(TNode t1, TNode t2) {
            WL("Q3");
            if (Q3Recurse(t1, t2)) WL("T");
            else WL("F");
        }
        static bool Q3Recurse(TNode t1, TNode t2) {
            if (t1.Value == t2.Value) return true;
            if (t1.Value != t2.Value) return false;
            return Q3Recurse(t1.LeftNode, t2.LeftNode) && Q3Recurse(t1.RightNode, t2.RightNode);
        }

        /// <summary>
        /// find # of elements of a tree in a range
        /// 
        /// is the range inclusive?
        /// 
        /// after thought: given that this is a binary tree, 
        /// if current node value is OUTSIDE of the range, 
        /// we only need to check either the left or the right tree because the remaining MUST be 0
        /// </summary>
        static void Q4(TNode t1, int min, int max) {
            WL(Q4Recurse(t1, min, max));
        }
        static int Q4Recurse(TNode t1, int min, int max) {
            return Q4Recurse(t1.LeftNode, min, max) +
                Q4Recurse(t1.RightNode, min, max) +
                (t1.Value >= 2 && t1.Value <= max ? 1 : 0);
        }

        /// <summary>
        /// question about traversing a tree
        /// 
        /// 3 scenarios: on the left most, on the right most, or in the middle
        /// </summary>
        static void Q5(TNode t1) {
        }

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
            WL("--Q7--");
            var c = new Q7Class();
            foreach (var value in values)
                c.AddElement(value);

            WL(c.NElementMean[elementCount] / elementCount);
        }

        /// <summary>
        /// running: O(N)
        /// space: O(1) ? why? bc no space is needed?
        /// </summary>
        static void Q8(List<Tuple<int, int>> input) {
            WL("--Q8--");
            var output = new List<Tuple<int, int>>();
            if (input.Count == 0) WL("None");
            else {
                var current = input[0];

                for (var i = 1; i < input.Count; i++) {
                    if (input[i].Item1 < current.Item2)
                        current = new Tuple<int,int>(current.Item1, Math.Max(current.Item2, input[i].Item2));
                    else {
                        output.Add(current);
                        current = input[i];
                    }
                }
                output.Add(current);
            }

            foreach (var item in output) {
                WL("(" + item.Item1 + "," + item.Item2 + ")");
            }
        }

        /// <summary>
        /// implement binary search
        /// </summary>
        static void Q9(List<int> input, int target) {
            WL("--Q9--");
            if (input.Count == 0) {
                WL("-1");
                return;
            }

            WL("Recursive");
            WL(Q9Recurse(input, target));
            WL("Iterative");
            WL(Q9Iter(input, target));
        }
        static int Q9Recurse(List<int> input, int target) {
            if (input.Count == 0) return -1;
            if (input.Count == 1)
                return input[0] == target ? 0 : -1;

            var mid = (int)Math.Floor((double)input.Count / 2);
            if (input[mid] == target) return mid;
            else {
                if (input[mid] < target) return Q9Recurse(input.Where(v => v > input[mid]).ToList(), target);
                else return Q9Recurse(input.Where(v => v < input[mid]).ToList(), target);
            }            
        }
        static int Q9Iter(List<int> input, int target) {
            var s = 0;
            var e = input.Count - 1;

            while (e >= s) {
                var m = (int)((s + e) / 2);

                if (input[m] == target) return m;
                else {
                    if (input[m] < target)
                        s = m + 1;
                    else
                        e = m - 1;
                }
            }

            return -1;
        }

        public static void Q10(List<int> input) {
            WL("--Q10--");
            if (input.Count == 1) { WL(input[0]); return; }
            var output = new List<int>();
            var down = false;

            for (var i = 1; i < input.Count; i++) {
                var currentDown = input[i] < input[i - 1];
                if (!currentDown && down)
                    output.Add(input[i - 1]);
                down = currentDown;
            }

            WL(string.Join(",", output));
            // TODO: need to finish recursive part, won't do right now because i already saw the solution
        }

        /// <summary>
        /// given a list of  int that will go up then go down, find the max value
        /// 
        /// so it absolutely cannot have dupplicate?
        /// </summary>
        public static void Q11(List<int> input) {
            WL("--Q11--");

            if (input.Count == 0) { WL("0"); return; }
            if (input.Count == 1) { WL(input[0]); return; }
            // easy way: O(N)
            for (var i = 1; i < input.Count; i++) {
                if (input[i] < input[i - 1]) { WL(input[i - 1]); return; }
            }
            WL(input[input.Count - 1]);
        }
        public static void Q11LogN(List<int> input) {
            WL("--Q11LogN--");
            // better way: O(logN)
            int s = 0, e = input.Count - 1;
            while (s <= e) {
                int m = (s + e) / 2;
                if ((m - 1) < 0 || (m + 1) >= input.Count) {
                    WL(input[m]);
                    return;
                }
                if (input[m] > input[m - 1] && input[m] > input[m + 1]) {
                    WL(input[m]);
                    return;
                }
                else if (input[m] < input[m - 1])
                    e = m - 1;
                else
                    s = m + 1;
            }
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

    public class TNode {
        public int Value { get; set; }
        public TNode LeftNode { get; set; }
        public TNode RightNode { get; set; }
        public TNode Parent { get; set; }

        public TNode() { }
        public TNode(int val) {
            Value = val;
        }
    }
}

/**
 * Note:
 * Q3 & Q4 are practice of recursion and basic tree structure
 **/
