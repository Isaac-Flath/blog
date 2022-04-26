#require "jupyter.notebook" ;;
(* #require "jupyter-archimedes" *)


exception Damn of string

let get_width_dir bw cw = 
  match compare cw bw  with
    |0 -> ""|1 -> "L"|(-1) -> "R"| _ -> raise (Damn "error")

let get_height_dir bh ch = 
  match compare ch bh with
    |0 -> "" |1 -> "U" |(-1) -> "D"| _ -> raise (Damn "error")

let get_direction currentloc bombloc = 
  let bw,bh = bombloc in
  let ((cw,ch),(_,_,_,_)) = currentloc in

  (get_height_dir bh ch) ^ (get_width_dir bw cw)

let take_step currentloc dir =
  let ((cw,ch),(w0,w1,h0,h1)) = currentloc in
  match dir with 
        |"L" -> (((w0+cw)/2,ch),(w0,cw,ch,ch))
        |"R" -> (((cw+w1)/2,ch),(cw,w1,ch,ch))
        |"U" -> ((cw,(h0+ch)/2),(cw,cw,h0,ch))
        |"D" -> ((cw,(ch+h1)/2),(cw,cw,ch,h1))
        |"UL" -> (((w0+cw)/2,(h0+ch)/2),(w0,cw,h0,ch))
        |"UR" -> (((cw+w1)/2,(w0+ch)/2),(cw,w1,h0,ch))
        |"DL" -> (((w0+cw)/2,(ch+h1)/2),(w0,cw,ch,h1))
        |"DR" -> (((cw+w1)/2,(ch+h1)/2),(cw,w1,ch,h1))
        |_ -> raise (Damn "error")

let print_step bl cl bd =
    let ((ow,oh),(bw1,bw2,bh1,bh2)) = cl in
    let bw, bh = bl in
    print_endline ("Board: " ^ string_of_int bw1 ^ "x"^ string_of_int bw2 ^ "x"^ string_of_int bh1 ^ "x"^ string_of_int bh2 ^ "  |  " ^
              "Bomb: " ^ string_of_int bw ^ "x" ^ string_of_int bh ^ "  |  " ^ 
              "Loc: " ^ string_of_int ow ^ "x" ^ string_of_int oh ^ "  |  " ^ 
              "Direction: " ^ bd);

let rec loop loc acc printf bl=
    let bombdir = get_direction loc bl in
    printf bl loc bombdir;

    let out = take_step loc bombdir in
    let ((ow,oh),(bw1,bw2,bh1,bh2)) = out in


    if (ow,oh)=(bl) then "success" 
    else if acc > 200 then "200 iters"
    else loop out (acc+1) printf bl

let sz = 1_000_000
let w,h = (Random.int sz,Random.int sz)
let current_loc = (Random.int w,Random.int h)
let bomb_loc = (Random.int w,Random.int h)
let board = (0,w,0,h)
let current_loc = (current_loc,board)

loop current_loc 0 print_step bomb_loc




