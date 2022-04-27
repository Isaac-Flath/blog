#require "jupyter.notebook" ;;
(* #require "jupyter-archimedes" *)


exception InvalidInput of string

let get_width_dir bw cw = 
  match compare cw bw  with
    |0 -> ""
    |1 -> "L"
    |(-1) -> "R"
    | _ -> raise (InvalidInput "error")

let get_height_dir bh ch = 
  match compare ch bh with
    |0 -> "" 
    |1 -> "U" 
    |(-1) -> "D"
    | _ -> raise (InvalidInput "error")

let get_direction loc target = 
  let bw,bh = target in
  let ((cw,ch),(_,_,_,_)) = loc in

  (get_height_dir bh ch) ^ (get_width_dir bw cw)

let take_step1 loc direction =
  let ((cw,ch),(w0,w1,h0,h1)) = loc in
  match direction with 
        |"L" -> (((w0+cw)/2,ch),(w0,cw,ch,ch))
        |"R" -> (((cw+w1)/2,ch),(cw,w1,ch,ch))
        |"U" -> ((cw,(h0+ch)/2),(cw,cw,h0,ch))
        |"D" -> ((cw,(ch+h1)/2),(cw,cw,ch,h1))
        |"UL" -> (((w0+cw)/2,(h0+ch)/2),(w0,cw,h0,ch))
        |"UR" -> (((cw+w1)/2,(w0+ch)/2),(cw,w1,h0,ch))
        |"DL" -> (((w0+cw)/2,(ch+h1)/2),(w0,cw,ch,h1))
        |"DR" -> (((cw+w1)/2,(ch+h1)/2),(cw,w1,ch,h1))
        |_ -> raise (InvalidInput "error")

let print_step target loc direction =
    let ((ow,oh),(bw1,bw2,bh1,bh2)) = loc in
    let bw, bh = target in
    print_endline ("Board: " ^ string_of_int bw1 ^ "x"^ string_of_int bw2 ^ "x"^ string_of_int bh1 ^ "x"^ string_of_int bh2 ^ "  |  " ^
              "Bomb: " ^ string_of_int bw ^ "x" ^ string_of_int bh ^ "  |  " ^ 
              "Loc: " ^ string_of_int ow ^ "x" ^ string_of_int oh ^ "  |  " ^ 
              "Direction: " ^ direction);

let rec loop loc printf target =
    let direction = get_direction loc target in
    printf target loc direction;

    let out = take_step1 loc direction in
    let ((ow,oh),(tw1,tw2,th1,th2)) = out in


    if (ow,oh)=(target) then "success" 
    else loop out printf target

let max_sz = 1_000_000
let w,h = (Random.int max_sz,Random.int max_sz)
let current_loc = (Random.int w,Random.int h)
let bomb_loc = (Random.int w,Random.int h)
let board = (0,w,0,h)
let current_loc = (current_loc,board)

loop current_loc print_step bomb_loc




