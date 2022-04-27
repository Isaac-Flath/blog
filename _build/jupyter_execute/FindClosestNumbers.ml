#require "jupyter.notebook" ;;

let rec create_list len =
    match len with
       |0 -> []
       |x -> Random.full_int max_int::create_list (len-1);;

let sorted_input = List.sort (fun x y -> x-y)

let difference_func (p,m) x = if abs(x-p)<m then (x,abs(x-p)) else (x,m);;
let final_calc = List.fold_left difference_func (max_int,max_int)

let _,min_diff = final_calc (sorted_input (create_list 100000))
