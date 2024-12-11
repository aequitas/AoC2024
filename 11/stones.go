package main2

import (
	"fmt"
	"strconv"
)

func blink(stones []int, blinks int) <-chan int {
	// fmt.Printf("%d %+v\n", blinks, stones)
	ch := make(chan int)

	go func() {
		defer close(ch)

		if blinks == 0 {
			for _, stone := range stones {
				ch <- stone
			}
			return
		}

		for _, stone := range(stones) {
			if stone == 0 {
				// fmt.Printf("%d, ->1\n", stone)
				for s := range blink([]int{1}, blinks - 1) {
					ch <- s
				}
			} else if s := strconv.Itoa(stone); len(s) % 2 == 0 {
				// fmt.Printf("%d, split\n", stone)
				mid := int(len(s)/2)
				left, _ := strconv.Atoi(s[:mid])
				right, _ := strconv.Atoi(s[mid:])
				for s := range blink([]int{left, right}, blinks - 1) {
					ch <- s
				}
			} else {
				// fmt.Printf("%d, *2024\n", stone)
				for stone := range blink([]int{stone*2024}, blinks -1) {
					ch <- stone
				}
			}
		}

		// for _, stone := range stones {
		// 	ch <- stone
		// }

		// stones
	}()
	return ch
}

func main() {
	var stones []int

	// stones = []int{125,17}
	stones = []int{5910927,0,1,47,261223,94788,545,7771}

	blinks := blink(stones, 75)

	count := 0
	for _ = range blinks {
		// fmt.Printf("%d ", stone)
		count++
	}
	fmt.Println()
	// fmt.Printf("stones %s\n", stones)
	fmt.Printf("stones %d\n", count)
}
