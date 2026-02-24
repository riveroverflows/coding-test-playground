package p46_permutations

fun permute(nums: IntArray): List<List<Int>> {
    val answer = mutableListOf<List<Int>>()
    val used = mutableSetOf<Int>()
    val curr = mutableListOf<Int>()
    backtrack(curr, nums, used, answer)
    return answer
}

fun backtrack(curr: MutableList<Int>, nums: IntArray, used: MutableSet<Int>, answer: MutableList<List<Int>>) {
    if (curr.size == nums.size) {
        answer.add(ArrayList(curr))
        return
    }
    for (num in nums) {
        if (num in used) continue
        curr.add(num)
        used.add(num)
        backtrack(curr, nums, used, answer)
        used.remove(num)
        curr.removeAt(curr.size - 1)
    }
}

fun main() {
    val line = readln()
    val nums = line.split(",").map { it.trim().toInt() }.toIntArray()
    println(permute(nums))
}