/*
Jhoan Buitrago
05/12/2023 dd/mm/yy

https://adventofcode.com/2023/day/5

Current solution: brute force

Solution idea: pre-transform ranges from location to seed
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
	dest   uint32
	source uint32
	len    uint32
}

func solve(seeds []uint32, conversionMap map[string][]RangeMap, keys []string) uint32 {
	var minLocation uint32 = math.MaxUint32

	for i := 0; i < (len(seeds)/2)+1; i += 2 {
		s := seeds[i]
		for j := seeds[i]; j < s+seeds[i+1]; j++ {
			conv := j
			for _, k := range keys {
				for _, rangeMap := range conversionMap[k] {
					leftS := rangeMap.source
					rightS := rangeMap.source + rangeMap.len - 1
					if conv >= leftS && conv <= rightS {
						conv = rangeMap.dest + (conv - leftS)
						break
					}
				}
				if j == 82 {
					fmt.Println(k, conv)
				}
			}

			if conv < minLocation {
				fmt.Println("Found lower seed:", j, conv, "\n")
				minLocation = conv
			}
		}
	}

	return minLocation
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)

	scanner.Scan()
	seedsLine := strings.TrimSpace(strings.Split(scanner.Text(), ":")[1])
	seedsStrings := strings.Split(seedsLine, " ")

	seeds := make([]uint32, len(seedsStrings))
	for i, s := range seedsStrings {
		tmp, _ := strconv.ParseUint(s, 10, 32)

		seeds[i] = uint32(tmp)
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
			d, _ := strconv.ParseUint(numbers[0], 10, 32)
			s, _ := strconv.ParseUint(numbers[1], 10, 32)
			l, _ := strconv.ParseUint(numbers[2], 10, 32)
			conversionMap[key] = append(conversionMap[key],
				RangeMap{uint32(d), uint32(s), uint32(l)})

			isNotEnd = scanner.Scan()
			line = scanner.Text()
		}
	}

	fmt.Println(solve(seeds, conversionMap, keys))
}
