object Main {
    const val MOD:Long = (1e9 + 7).toLong();
    private fun binPow (x:Long, y:Int) : Long{
        var gamma = y
        var res:Long = x
        var ans:Long = 1
        while (gamma > 0) {
            if (gamma % 2 == 1) {
                ans = mult(ans,res)
            }
            res = mult(res, res)
            gamma /= 2
        }
        return ans;
    }
    fun inverse (x:Long) : Long {
        return binPow(x, (MOD - 2).toInt());
    }
    private val factorial = arrayListOf<Long>()
    fun mult (x:Long, y:Long): Long {
        return (x * y) % MOD;
    }
    fun add (x:Long, y:Long) : Long {
        return (x + y) % MOD;
    }
    fun f (n: Int) : Long {
        var ans:Long = 0;
        var prev: Long = 2
        var cur: Long = 1
        var n1: Long = 1
        var n2: Long = 1;
        for (i in 1 until n - 1) {
            n2 = mult(n2, i.toLong());
            n1 = mult(n1, i.toLong())
        }
        n1 = mult(n1, ((n - 1).toLong()));
        var f1: Long = 1;
        for (i in 1 until 2 * (n - 2) + 1) {
            f1 = mult(f1, i.toLong())
        }
        var f2:Long = n2
        for (i in n - 2 downTo 0) {
            cur = add(cur, prev) // cur = cur + prev
            prev = add(cur, MOD - prev)
            val left:Long = mult(f1, mult(inverse(f2), inverse(n2)));
            val right:Long = if (i != 0) {
                mult(f1, mult(mult(inverse(f2), i.toLong()), inverse(n1)))
            } else {
                0
            }
            f1 = mult(f1, inverse((n - 2 + i).toLong()))
            f2 = mult(f2, inverse(i.toLong()))
            val value:Long = add(left, MOD - right)
            ans = add(ans, mult(value, cur))
        }
        return ans;
    }
    fun main() {
        val mx = 100000000
        println(f(mx))
    }
}
fun main(args: Array<String>) {
    println("Hello world!")
    Main.main()
}
