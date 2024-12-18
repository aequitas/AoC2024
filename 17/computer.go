package main

import (
	"fmt"
	"time"
	// "sync"
)

func run(a uint64, b uint64, c uint64, program []uint8, check []uint8 ) bool {
	ip := uint8(0)
	output := []uint8{}

	if len(check) == 0 {
		check = program
	}

	for ip < uint8(len(program)) {
		// fmt.Printf("%20d %20d %20d %20.d %v\n", a,b,c,ip,output)
		opcode := program[ip]
		combo := uint64(program[ip+1])

		if combo == 4 {
			combo = a
		} else if combo == 5 {
			combo = b
		} else if combo == 6 {
			combo = c
		}

		switch opcode {
			case 0:
				a = a / (1 <<combo)
			case 1:
				b = b ^ uint64(program[ip+1])
			case 2:
				b = uint64(combo % 8)
			case 3:
				if a != 0 {
					ip = program[ip+1]
					continue
				}
			case 4:
				b = b ^ c
			case 5:
				if check[len(output)] != uint8(combo % 8) {
					return false
				}
				output = append(output, uint8(combo % 8))
				// fmt.Println()
				// fmt.Printf("%20d %20d %20d %20.d %v\n", a,b,c,ip,output)

				if len(output) == len(check){
					return true
				}
			case 6:
				b = a / (1<<combo)
			case 7:
				c = a / (1<<combo)
		}

		ip += 2
	}

	return false
}

// func main(){
// 	start := time.Now()
// 	for i := uint64(0); i <= 18446744073709551615; i+=8 {
// 		if run(i, 0, 0, []uint8{0,3,5,4,3,0}){
// 			fmt.Println(i)
// 			break
// 		}
// 	}
// 	fmt.Println(time.Since(start))

// 	for i := uint64(4294967295); i <= 18446744073709551615; i+=8 {
// 		if run(i, 0, 0, []uint8{2,4,1,1,7,5,0,3,1,4,4,5,5,5,3,0}){
// 			fmt.Println(i)
// 			break
// 		}
// 	}
// }

// func loop(start uint64, end uint64){
// 	for i := uint64(start); i <= end; i++ {
// 		if run(i, 0, 0, []uint64{2,4,1,1,7,5,0,3,1,4,4,5,5,5,3,0}){
// 			fmt.Println(i)
// 			break
// 		}
// 	}
// }

func main(){
	start := time.Now()
	for i := uint64(0); i <= 18446744073709551615; i += 64 {
		if run(i, 0, 0, []uint8{0,3,5,4,3,0}, []uint8{})  {
			fmt.Println(i)
			break
		}
	}
	fmt.Println(time.Since(start))


	{
		start := time.Now()
		if ! run(51571418, 0, 0, []uint8{2,4,1,1,7,5,0,3,1,4,4,5,5,5,3,0}, []uint8{4,0,4,7,1,2,7,1,6}) {
			panic(1)
		}
		fmt.Println(time.Since(start))
	}
	{
		start := time.Now()
		if ! run(202322348616234, 0, 0, []uint8{2,4,1,1,7,5,0,3,1,4,4,5,5,5,3,0}, []uint8{}) {
			panic(1)
		}
		fmt.Println(time.Since(start))
	}

	program := []uint8{2,4,1,1,7,5,0,3,1,4,4,5,5,5,3,0}
	x := uint64(0)
	for j := len(program) - 1; j > 0; j-- {
		for i := uint64(x); i < 1<<63; i++  {
			if run(i, 0, 0, program, program[j:]) {
				fmt.Println(i)
				x = i*uint64(len(program)/2)
				break
			}
		}
	}
	{
		program := []uint8{0,3,5,4,3,0}
		x := uint64(0)
		for j := len(program); j > 0; j-- {
			for i := uint64(x); i < 1<<63; i++  {
				if run(i, 0, 0, program, program[j-1:]) {
					fmt.Println(i)
					x = i*uint64(len(program)/2)
					break
				}
			}
		}

	}

	// {
	// 	for i := uint64(40); i < 1<<63; i++  {
	// 		if run(i, 0, 0, []uint8{2,4,1,1,7,5,0,3,1,4,4,5,5,5,3,0}, []uint8{3,0}) {
	// 			fmt.Println(i)
	// 			break
	// 		}
	// 	}
	// }

	// {
	// 	for i := uint64(46); i < 1<<63; i++  {
	// 		if run(i, 0, 0, []uint8{2,4,1,1,7,5,0,3,1,4,4,5,5,5,3,0}, []uint8{5,3,0}) {
	// 			fmt.Println(i)
	// 			break
	// 		}
	// 	}
	// }

	// {
	// start := time.Now()
	// for i := uint64(0); i <= 18446744073709551615; i += 117440 {
	// 	if run(i, 0, 0, []uint8{0,3,5,4,3,0}){
	// 		fmt.Println(i)
	// 	}
	// }
	// fmt.Println(time.Since(start))
	// }
	// {
	// 	ch := make(chan uint64)

	// 	start := time.Now()
	// 	for i := uint64(0); i <= 117440*2; i = i + 117440*2 / 4 {

	// 		go func(start uint64, end uint64){
	// 			for i := start; i < end; i=i+8 {
	// 				if run(i, 0, 0, []uint8{0,3,5,4,3,0}){
	// 					// fmt.Println(i)
	// 					ch <- i
	// 					// close(ch)
	// 				}
	// 			}

 // 			}(i, i + 117440*2 / 4)
	// 	}
	// 	for i := range ch {
	// 		fmt.Println(i)
	// 		close(ch)
	// 	}
	// 	fmt.Println(time.Since(start))
	// }

	// {
	// 	ch := make(chan uint64)
	// 	for i := uint64(44); i < 50; i++  {
	// 		start := uint64(1<<i)
	// 		end := uint64(1<<(i+1))

	// 		go func(start uint64, end uint64){
	// 			fmt.Println(start, end)
	// 			for i := start; i < end; i=i+8 {
	// 				if run(i, 0, 0, []uint8{2,4,1,1,7,5,0,3,1,4,4,5,5,5,3,0}){
	// 					fmt.Println(i)
	// 					ch <- i
	// 				}
	// 			}
	// 			ch <- 0
 // 			}(start, end)
	// 	}
	// 	for i := range ch {
	// 		fmt.Println(i)
	// 	}
	// }

	// {
	// 	var wg sync.WaitGroup
	// 	ch := make(chan uint64)
	// 	max := uint64(1<<63)
	// 	for i := max; i > 0; i = i / 2  {
	// 		fmt.Println(i, max/i)
	// 		// fmt.Println()
	// 		for j := max; j > 0; j = j + i {
	// 			start := j+i
	// 			end := j
	// 			step := i
	// 			// fmt.Println(start,end, step)

	// 			wg.Add(1)
	// 			go func(start uint64, end uint64){
	// 				defer wg.Done()
	// 				for x := start ; x < end; x+=step*2 {
	// 					if run(x, 0, 0, []uint8{2,4,1,1,7,5,0,3,1,4,4,5,5,5,3,0}, []uint8{}){
	// 						fmt.Println(x)
	// 						ch <- x
	// 					}
	// 				}
	//  			}(start, end)

	// 		}
	// 	}
	// 		// for j := uint64(0); j < 1<<62; j+=i {
	// 		// fmt.Println(j)
	// 		// start := uint64(j<<i)
	// 		// end := uint64(j<<(i+1))
	// 		// fmt.Println(start, end)
	// 		// // fmt.Println(i)
	// 	go func() { wg.Wait(); close(ch)}()
	// 	for i := range ch {
	// 		fmt.Println(i)
	// 	}
	// }
}
