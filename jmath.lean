-- 1. THE J-PLANE
structure JNum where
  a : Int
  b : Int
  deriving Repr, BEq

def J_zero : JNum := { a := 0, b := 0 }
def J : JNum := { a := 0, b := 1 }

-- 2. OPERATIONS
def mul_JNum (x y : JNum) : JNum :=
  match x, y with
  | { a := _, b := xb }, { a := 0, b := 0 } => { a := xb, b := 0 }
  | { a := 0, b := 0 }, { a := _, b := yb } => { a := yb, b := 0 }
  | { a := xa, b := xb }, { a := ya, b := yb } => { a := xa * ya, b := xa * yb + xb * ya + xb * yb }

instance : Mul JNum where
  mul := mul_JNum

instance : Add JNum where
  add x y := { a := x.a + y.a, b := x.b + y.b }

-- 3. AXIOM VERIFICATION 
theorem j_squared_eq_j : J * J = J := by 
  rfl

theorem absolute_zero_extraction (xa xb : Int) : 
  ({ a := xa, b := xb } : JNum) * J_zero = { a := xb, b := 0 } := by 
  rfl

-- 4. THE TRILOGY OF PROOFS
def evaluate_UGF (f0 f1 : Int) : JNum :=
  { a := f0, b := f1 - f0 }

def F (m c x : Int) : Int :=
  m * x + c

theorem anchor_zero (m c : Int) : F m c 0 = c := by
  simp +arith [F]

theorem anchor_one (m c : Int) : F m c 1 = m + c := by
  simp +arith [F]

theorem structural_gradient (m c : Int) : F m c 1 - F m c 0 = m := by
  simp +arith [F]

theorem derive_UGF (m c : Int) : evaluate_UGF (F m c 0) (F m c 1) = { a := c, b := m } := by
  simp +arith [F, evaluate_UGF]
