package main

import (
	"bufio"
	"os"
	"strconv"
	"unicode"
)

const size = 8

var rowChange = [size]int{-1, -1, -1, 0, 0, 1, 1, 1}
var colChange = [size]int{-1, 0, 1, -1, 1, -1, 0, 1}

func scanNeighbors(matrix []string, visited [][]bool, row int, col int) int {
	sum := 0
	n := len(matrix)
	m := len(matrix[0])

	for i := 0; i < size; i++ {
		curRow := row + rowChange[i]
		curCol := col + colChange[i]

		// Must be inside bounds, be a digit and not visited.
		if curRow >= 0 && curRow < n && curCol >= 0 && curCol < m &&
			unicode.IsDigit(rune(matrix[curRow][curCol])) && !visited[curRow][curCol] {

			visited[curRow][curCol] = true

			leftmost := curCol
			for leftmost-1 >= 0 && unicode.IsDigit(rune(matrix[curRow][leftmost-1])) {
				leftmost--
				visited[curRow][leftmost] = true
			}

			rightmost := curCol
			for rightmost+1 < m && unicode.IsDigit(rune(matrix[curRow][rightmost+1])) {
				rightmost++
				visited[curRow][rightmost] = true
			}

			tmp, _ := strconv.Atoi(matrix[curRow][leftmost : rightmost+1])
			sum += tmp
		}
	}

	return sum
}

func solve(matrix []string) int {
	total := 0
	n := len(matrix)
	m := len(matrix[0])
	visited := make([][]bool, n)

	// init visited with false
	for i := 0; i < n; i++ {
		visited[i] = make([]bool, m)

		for j := 0; j < n; j++ {
			visited[i][j] = false
		}
	}

	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			c := matrix[i][j]
			if !unicode.IsDigit(rune(c)) && c != '.' {
				total += scanNeighbors(matrix, visited, i, j)
			}
		}
	}

	return total
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)

	matrix := []string{}

	for scanner.Scan() {
		line := scanner.Text()
		matrix = append(matrix, line)
	}

	total := solve(matrix)
	println("total:", total)

}
