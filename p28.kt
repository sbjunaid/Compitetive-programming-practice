fun findUniqueElementIndex(arr: List<Int>): Int {
    // Iterate through the array and find the unique element
    var uniqueElement: Int? = null
    for (num in arr) {
        if (arr.count { it == num } == 1) {
            uniqueElement = num
            break
        }
    }

    // Find the index of the unique element
    val uniqueIndex = arr.indexOf(uniqueElement) + 1

    return uniqueIndex
}

fun main() {
    val t = readLine()!!.toInt()
    repeat(t) {
        val n = readLine()!!.toInt()
        val array = readLine()!!.split(" ").map { it.toInt() }
        val result = findUniqueElementIndex(array)
        println(result)
    }
}
