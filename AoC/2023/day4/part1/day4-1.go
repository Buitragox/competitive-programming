/*
Jhoan Buitrago
05/12/2023 dd/mm/yy

https://adventofcode.com/2023/day/4
*/

package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"slices"
	"strconv"
	"strings"
)

func solve(matrixWin [][]int, matrixCur [][]int) int {
	total := 0

	for i, currents := range matrixCur {
		points := 0
		for _, cur := range currents {
			isWinning := slices.Contains(matrixWin[i], cur)

			if isWinning {
				if points > 0 {
					points *= 2
				} else {
					points = 1
				}
			}
		}

		total += points
	}

	return total
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)

	matrixWin := [][]int{}
	matrixCur := [][]int{}
	i := 0
	regex := regexp.MustCompile(`\s+`)

	for scanner.Scan() {
		line := strings.Split(scanner.Text(), ":")[1]
		split := strings.Split(line, "|")
		winnings := regex.Split(strings.TrimSpace(split[0]), -1)
		currents := regex.Split(strings.TrimSpace(split[1]), -1)

		//winningsInt := make(type, 0)

		matrixWin = append(matrixWin, []int{})
		for j := 0; j < len(winnings); j++ {
			tmp, _ := strconv.Atoi(winnings[j])
			matrixWin[i] = append(matrixWin[i], tmp)
		}

		matrixCur = append(matrixCur, []int{})
		for j := 0; j < len(currents); j++ {
			tmp, _ := strconv.Atoi(currents[j])
			matrixCur[i] = append(matrixCur[i], tmp)
		}

		i++
	}

	total := solve(matrixWin, matrixCur)
	fmt.Println("total:", total)

}
