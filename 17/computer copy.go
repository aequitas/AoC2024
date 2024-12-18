package main

import (
	"fmt"
	"time"
)

func run2(a uint64, b uint64, c uint64, program []uint64) bool {
	ip := uint64(0)
	output := []uint64{}

	for ip < uint64(len(program)) {
		opcode := program[ip]
		combo := program[ip+1]

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
				b = b ^ program[ip+1]
			case 2:
				b = combo % 8
			case 3:
				if a != 0 {
					ip = program[ip+1]
					continue
				}
			case 4:
				b = b ^ c
			case 5:
				output = append(output, combo % 8)

				for i := 0; i < len(output); i++ {
					if output[i] != program[i] {
						return false
					}
				}
				if len(output) == len(program){
					// fmt.Println("answer", output)
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
// 	for i := uint64(0); i <= 18446744073709551615; i++ {
// 		if run(i, 0, 0, []uint64{0,3,5,4,3,0}){
// 			fmt.Println(i)
// 			break
// 		}
// 	}
// 	fmt.Println(time.Since(start))

// 	for i := uint64(0); i <= 18446744073709551615; i++ {
// 		if run(i, 0, 0, []uint64{2,4,1,1,7,5,0,3,1,4,4,5,5,5,3,0}){
// 			fmt.Println(i)
// 			break
// 		}
// 	}
// }
