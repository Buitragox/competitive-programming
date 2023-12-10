/*
Jhoan Buitrago
05/12/2023 dd/mm/yy

https://adventofcode.com/2023/day/5
*/

package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

type RangeMap struct {
	dest   int
	source int
	len    int
}

func solve(seeds []int, conversionMap map[string][]RangeMap, keys []string) int {
	minLocation := math.MaxInt32

	for _, s := range seeds {
		conv := s
		for _, k := range keys {
			for _, rangeMap := range conversionMap[k] {
				leftS := rangeMap.source
				rightS := rangeMap.source + rangeMap.len - 1
				if conv >= leftS && conv <= rightS {
					conv = rangeMap.dest + (conv - leftS)
					break
				}
			}
		}

		if conv < minLocation {
			minLocation = conv
		}
	}

	return minLocation
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)

	scanner.Scan()
	seedsLine := strings.TrimSpace(strings.Split(scanner.Text(), ":")[1])
	seedsStrings := strings.Split(seedsLine, " ")

	seeds := make([]int, len(seedsStrings))
	for i, s := range seedsStrings {
		tmp, _ := strconv.Atoi(s)
		seeds[i] = tmp
	}

	// Delete empty line
	scanner.Scan()
	scanner.Text()

	keys := make([]string, 0, 7)
	conversionMap := map[string][]RangeMap{}

	for scanner.Scan() {
		key := strings.Split(scanner.Text(), " ")[0]
		//fmt.Println(key)
		keys = append(keys, key)
		conversionMap[key] = make([]RangeMap, 0)

		isNotEnd := scanner.Scan()
		line := scanner.Text()
		for isNotEnd && line != "" {
			//fmt.Println(line)
			numbers := strings.Split(line, " ")
			d, _ := strconv.Atoi(numbers[0])
			s, _ := strconv.Atoi(numbers[1])
			l, _ := strconv.Atoi(numbers[2])
			conversionMap[key] = append(conversionMap[key], RangeMap{d, s, l})

			isNotEnd = scanner.Scan()
			line = scanner.Text()
		}
	}

	fmt.Println(solve(seeds, conversionMap, keys))
}
