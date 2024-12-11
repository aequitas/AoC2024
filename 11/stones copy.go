package main

import (
	"fmt"
	"strconv"
)

// var cache [2024*2024]int
var cache [76]map[int]int

func blink(stones []int, blinks int) int {
	// fmt.Printf("%d %+v\n", 6-blinks, stones)
	if blinks <= 0 {
		return len(stones)
	}

	count := 0
	var stone int
	for _, stone = range(stones) {
		if cache[blinks][stone] != 0 {
			// fmt.Printf("cache %d %d %+v\n\n\n\n", blinks, stone, cache)
			count += cache[blinks][stone]
			continue
		}
		if stone == 0 {
			if blinks == 1 {
				count += 1
				continue
			}
			if blinks == 2 {
				count += 1
				continue
			}
			i := blink([]int{20,24}, blinks - 3)
			count += i
			continue
		}
		// if stone < 2024*2024 && cache[stone] != 0 {
		// 	count += cache[stone]
		// 	continue
		// }
		if s := strconv.Itoa(stone); len(s) % 2 == 0 {
			mid := int(len(s)/2)
			left, _ := strconv.Atoi(s[:mid])
			right, _ := strconv.Atoi(s[mid:])
			i := blink([]int{left, right}, blinks -1)
			count += i
			continue
		}
		i := blink([]int{stone * 2024}, blinks - 1)
		// fmt.Printf("%d %d\n", stone, i)
		cache[blinks][stone] = i
		count += i
	}
	return count
}

func main() {
	// cache = [2048*2048]int{}
	for i := range(76) {
		cache[i] = make(map[int]int)
	}

	var stones []int

	// stones = []int{125,17}
	// fmt.Printf("22\t\t%d\n", blink(stones, 6))

	// fmt.Printf("55312\t\t%d\n", blink(stones, 25))


	// stones = []int{5910927,0,1,47,261223,94788,545,7771}
	// fmt.Printf("193607\t\t%d\n", blink(stones, 25))


	fmt.Printf("193607\t\t%d\n", blink(stones, 75))
}
