/*
Jhoan Buitrago
03/12/2023 dd/mm/yy

https://adventofcode.com/2023/day/3
*/

package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"unicode"
)

const size = 8

var rowChange = [size]int{-1, -1, -1, 0, 0, 1, 1, 1}
var colChange = [size]int{-1, 0, 1, -1, 1, -1, 0, 1}

func visit(visited [][]bool, visitedHistory [][]int, i int, j int) ([][]bool, [][]int) {
	visited[i][j] = true
	visitedHistory = append(visitedHistory, []int{i, j})
	return visited, visitedHistory
}

func scanNeighbors(matrix []string, visited [][]bool, row int, col int) (int, bool) {
	gearRatio := 1
	n := len(matrix)
	m := len(matrix[0])
	numCount := 0
	visitedHistory := [][]int{}

	for i := 0; i < size; i++ {
		curRow := row + rowChange[i]
		curCol := col + colChange[i]

		// Must be inside bounds, be a digit and not visited.
		if curRow >= 0 && curRow < n && curCol >= 0 && curCol < m &&
			unicode.IsDigit(rune(matrix[curRow][curCol])) && !visited[curRow][curCol] {

			//fmt.Println("found new number in", curRow, curCol)

			numCount++
			if numCount > 2 {
				break
			}

			visited, visitedHistory = visit(visited, visitedHistory, curRow, curCol)

			leftmost := curCol
			for leftmost-1 >= 0 && unicode.IsDigit(rune(matrix[curRow][leftmost-1])) {
				leftmost--
				visited, visitedHistory = visit(visited, visitedHistory, curRow, leftmost)
			}

			rightmost := curCol
			for rightmost+1 < m && unicode.IsDigit(rune(matrix[curRow][rightmost+1])) {
				rightmost++
				visited, visitedHistory = visit(visited, visitedHistory, curRow, rightmost)
			}

			tmp, _ := strconv.Atoi(matrix[curRow][leftmost : rightmost+1])
			//fmt.Println(tmp)
			gearRatio *= tmp
		}
	}

	isGear := true

	if numCount != 2 {
		isGear = false
		for _, position := range visitedHistory {
			visited[position[0]][position[1]] = false
		}
	}

	return gearRatio, isGear
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
			if c == '*' {
				gearRatio, isGear := scanNeighbors(matrix, visited, i, j)

				if isGear {
					total += gearRatio
				}
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
	fmt.Println("total:", total)

}
