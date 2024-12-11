package main3

import (
	"fmt"
	"strconv"
	"sync"
)

var cache [2048*2048]int
var mutex = sync.RWMutex{}

func blink(stones []int, blinks int) <-chan int {
	// fmt.Printf("%d %+v\n", blinks, stones)
	ch := make(chan int)

	go func() {
		defer close(ch)

		if blinks == 0 {
			// fmt.Printf("%d\n", len(stones))
			ch <- len(stones)
			// for _, stone := range stones {
			// 	ch <- stone
			// }
			return
		}

		for _, stone := range(stones) {
			mutex.Lock()
			fmt.Printf("%+v\n", cache)
			if i := cache[stone]; i != 0 {
				mutex.Unlock()
				ch <- i
			} else {
				mutex.Unlock()
			}

			if stone == 0 {
				// fmt.Printf("%d, ->1\n", stone)
				for s := range blink([]int{1}, blinks - 1) {
					mutex.Lock()
					cache[stone] = s
					mutex.Unlock()
					ch <- s
				}
				return
			}
			if s := strconv.Itoa(stone); len(s) % 2 == 0 {
				// fmt.Printf("%d, split\n", stone)
				mid := int(len(s)/2)
				left, _ := strconv.Atoi(s[:mid])
				right, _ := strconv.Atoi(s[mid:])
				for s := range blink([]int{left, right}, blinks - 1) {
					mutex.Lock()
					cache[stone] = s
					mutex.Unlock()
					ch <- s
				}
				return
			}

			// fmt.Printf("%d, *2024\n", stone)
			for stone := range blink([]int{stone*2024}, blinks -1) {
				mutex.Lock()
				cache[stone] = stone
				mutex.Unlock()
				ch <- stone
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
	// cache = [2048*2048]int{}

	var stones []int

	stones = []int{125,17}
	blinks := blink(stones, 25)

	// stones = []int{5910927,0,1,47,261223,94788,545,7771}
	// blinks := blink(stones, 75)


	count := 0
	for stone := range blinks {
		// fmt.Printf("%d ", stone)
		count += stone
	}
	fmt.Println()
	fmt.Printf("stones %d\n", count)



	// fmt.Printf("stones %d\n", count)

}
