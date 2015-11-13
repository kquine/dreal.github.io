
from gen import *

##########
# shared #
##########

flow_var[0] = """
(declare-fun tau () Real)
"""

flow_dec[0] = """
(define-ode flow_1 ((= d/dt[tau] 1)))
"""

state_dec[0] = """
(declare-fun time_{0} () Real)  
(declare-fun tau_{0}_0 () Real) 
(declare-fun tau_{0}_t () Real) 
"""

state_val[0] = """
(assert (<= 0 time_{0}))  (assert (<= time_{0} 0.1))
(assert (<= 0 tau_{0}_0)) (assert (<= tau_{0}_0 50))
(assert (<= 0 tau_{0}_t)) (assert (<= tau_{0}_t 50))
(assert (=> (or mode1L_{0} mode2L_{0} mode3L_{0}) (or mode1U_{0} mode2U_{0} mode3U_{0})))
"""

cont_cond[0] = ["""
(assert (and (= [d1_{0}_t g1_{0}_t d2_{0}_t g2_{0}_t d3_{0}_t g3_{0}_t tau_{0}_t] 
             (pintegral 0. time_{0} 
	                [d1_{0}_0 g1_{0}_0 d2_{0}_0 g2_{0}_0 d3_{0}_0 g3_{0}_0 tau_{0}_0] 
			[holder_{1} holder_{2} holder_{3} holder_{4}]))
             (connect holder_{4} flow_1)))"""]

jump_cond[0] = ["""
(assert (= tau_{1}_0 tau_{0}_t))"""]

#############
# battery 1 #
#############

flow_var[1] = """
(declare-fun d1 () Real)
(declare-fun g1 () Real)
"""

flow_dec[1] = """
(define-ode flow_2 ((= d/dt[d1] (- (/ (/ 1 3) 0.166) (* 0.122 d1))) (= d/dt[g1] (- 0 (/ 1 3)))))
(define-ode flow_3 ((= d/dt[d1] (- (/ 0.5 0.166) (* 0.122 d1))) (= d/dt[g1] -0.5)))
(define-ode flow_4 ((= d/dt[d1] (- (/ 1 0.166) (* 0.122 d1))) (= d/dt[g1] -1)))
(define-ode flow_5 ((= d/dt[d1] (- 0 (* 0.122 d1))) (= d/dt[g1] 0)))
(define-ode flow_6 ((= d/dt[d1] 0) (= d/dt[g1] 0)))
"""

state_dec[1] = """
(declare-fun mode1L_{0} () Bool) 
(declare-fun mode1U_{0} () Bool) 
(declare-fun d1_{0}_0 () Real)  
(declare-fun d1_{0}_t () Real)  
(declare-fun g1_{0}_0 () Real)  
(declare-fun g1_{0}_t () Real)  
"""

state_val[1] = """
(assert (<= -10 d1_{0}_0)) (assert (<= d1_{0}_0 10))
(assert (<= -10 d1_{0}_t)) (assert (<= d1_{0}_t 10))
(assert (<= -10 g1_{0}_0)) (assert (<= g1_{0}_0 10))
(assert (<= -10 g1_{0}_t)) (assert (<= g1_{0}_t 10))
(assert (=> mode1U_{0} mode1L_{0}))
"""

cont_cond[1] = ["""
(assert (or (and mode1L_{0} mode1U_{0}     (and mode2U_{0} mode3U_{0})  (connect holder_{1} flow_2))
            (and mode1L_{0} mode1U_{0}     (xor mode2U_{0} mode3U_{0})  (connect holder_{1} flow_3))
            (and mode1L_{0} mode1U_{0} (not (or mode2U_{0} mode3U_{0})) (connect holder_{1} flow_4))
            (and mode1L_{0} (not mode1U_{0})                            (connect holder_{1} flow_5))
            (and (not mode1L_{0})                                       (connect holder_{1} flow_6))))
(assert (not (and (connect holder_{1} flow_2) (connect holder_{1} flow_3))))
(assert (not (and (connect holder_{1} flow_2) (connect holder_{1} flow_4))))
(assert (not (and (connect holder_{1} flow_2) (connect holder_{1} flow_5))))
(assert (not (and (connect holder_{1} flow_2) (connect holder_{1} flow_6))))
(assert (not (and (connect holder_{1} flow_3) (connect holder_{1} flow_4))))
(assert (not (and (connect holder_{1} flow_3) (connect holder_{1} flow_5))))
(assert (not (and (connect holder_{1} flow_3) (connect holder_{1} flow_6))))
(assert (not (and (connect holder_{1} flow_4) (connect holder_{1} flow_5))))
(assert (not (and (connect holder_{1} flow_4) (connect holder_{1} flow_6))))
(assert (not (and (connect holder_{1} flow_5) (connect holder_{1} flow_6))))"""]

jump_cond[1] = ["""
(assert (and (= d1_{1}_0 d1_{0}_t) (= g1_{1}_0 g1_{0}_t)))
(assert (or (and (<= g1_{0}_t (* (- 1 0.166) d1_{0}_t)) 
                 (= mode1L_{1} false) (= mode1U_{1} false))
            (and (>  g1_{0}_t (* (- 1 0.166) d1_{0}_t)) 
                 (= mode1U_{0} true)
                 (= mode1L_{1} true))))"""]

#############
# battery 2 #
#############

flow_var[2] = """
(declare-fun d2 () Real)
(declare-fun g2 () Real)
"""

flow_dec[2] = """
(define-ode flow_7  ((= d/dt[d2] (- (/ (/ 1 3) 0.166) (* 0.122 d2))) (= d/dt[g2] (- 0 (/ 1 3)))))
(define-ode flow_8  ((= d/dt[d2] (- (/ 0.5 0.166) (* 0.122 d2))) (= d/dt[g2] -0.5)))
(define-ode flow_9  ((= d/dt[d2] (- (/ 1 0.166) (* 0.122 d2))) (= d/dt[g2] -1)))
(define-ode flow_10 ((= d/dt[d2] (- 0 (* 0.122 d2))) (= d/dt[g2] 0)))
(define-ode flow_11 ((= d/dt[d2] 0) (= d/dt[g2] 0)))
"""

state_dec[2] = """
(declare-fun mode2L_{0} () Bool) 
(declare-fun mode2U_{0} () Bool) 
(declare-fun d2_{0}_0 () Real)  
(declare-fun d2_{0}_t () Real)  
(declare-fun g2_{0}_0 () Real)  
(declare-fun g2_{0}_t () Real)  
"""

state_val[2] = """
(assert (<= -10 d2_{0}_0)) (assert (<= d2_{0}_0 10))
(assert (<= -10 d2_{0}_t)) (assert (<= d2_{0}_t 10))
(assert (<= -10 g2_{0}_0)) (assert (<= g2_{0}_0 10))
(assert (<= -10 g2_{0}_t)) (assert (<= g2_{0}_t 10))
(assert (=> mode2U_{0} mode2L_{0}))
"""

cont_cond[2] = ["""
(assert (or (and mode2L_{0} mode2U_{0}     (and mode1U_{0} mode3U_{0})  (connect holder_{2} flow_7))
            (and mode2L_{0} mode2U_{0}     (xor mode1U_{0} mode3U_{0})  (connect holder_{2} flow_8))
            (and mode2L_{0} mode2U_{0} (not (or mode1U_{0} mode3U_{0})) (connect holder_{2} flow_9))
            (and mode2L_{0} (not mode2U_{0})                            (connect holder_{2} flow_10))
            (and (not mode2L_{0})                                       (connect holder_{2} flow_11))))
(assert (not (and (connect holder_{2} flow_7)  (connect holder_{2} flow_8))))
(assert (not (and (connect holder_{2} flow_7)  (connect holder_{2} flow_9))))
(assert (not (and (connect holder_{2} flow_7)  (connect holder_{2} flow_10))))
(assert (not (and (connect holder_{2} flow_7)  (connect holder_{2} flow_11))))
(assert (not (and (connect holder_{2} flow_8)  (connect holder_{2} flow_9))))
(assert (not (and (connect holder_{2} flow_8)  (connect holder_{2} flow_10))))
(assert (not (and (connect holder_{2} flow_8)  (connect holder_{2} flow_11))))
(assert (not (and (connect holder_{2} flow_9)  (connect holder_{2} flow_10))))
(assert (not (and (connect holder_{2} flow_9)  (connect holder_{2} flow_11))))
(assert (not (and (connect holder_{2} flow_10) (connect holder_{2} flow_11))))"""]

jump_cond[2] = ["""
(assert (and (= d2_{1}_0 d2_{0}_t) (= g2_{1}_0 g2_{0}_t)))
(assert (or (and (<= g2_{0}_t (* (- 1 0.166) d2_{0}_t)) 
                 (= mode2L_{1} false) (= mode2U_{1} false))
            (and (>  g2_{0}_t (* (- 1 0.166) d2_{0}_t)) 
                 (= mode2U_{0} true)
                 (= mode2L_{1} true))))"""]

#############
# battery 3 #
#############

flow_var[3] = """
(declare-fun d3 () Real)
(declare-fun g3 () Real)
"""

flow_dec[3] = """
(define-ode flow_12 ((= d/dt[d3] (- (/ (/ 1 3) 0.166) (* 0.122 d3))) (= d/dt[g3] (- 0 (/ 1 3)))))
(define-ode flow_13 ((= d/dt[d3] (- (/ 0.5 0.166) (* 0.122 d3))) (= d/dt[g3] -0.5)))
(define-ode flow_14 ((= d/dt[d3] (- (/ 1 0.166) (* 0.122 d3))) (= d/dt[g3] -1)))
(define-ode flow_15 ((= d/dt[d3] (- 0 (* 0.122 d3))) (= d/dt[g3] 0)))
(define-ode flow_16 ((= d/dt[d3] 0) (= d/dt[g3] 0)))
"""

state_dec[3] = """
(declare-fun mode3L_{0} () Bool) 
(declare-fun mode3U_{0} () Bool) 
(declare-fun d3_{0}_0 () Real)  
(declare-fun d3_{0}_t () Real)  
(declare-fun g3_{0}_0 () Real)  
(declare-fun g3_{0}_t () Real)  
"""

state_val[3] = """
(assert (<= -10 d3_{0}_0)) (assert (<= d3_{0}_0 10))
(assert (<= -10 d3_{0}_t)) (assert (<= d3_{0}_t 10))
(assert (<= -10 g3_{0}_0)) (assert (<= g3_{0}_0 10))
(assert (<= -10 g3_{0}_t)) (assert (<= g3_{0}_t 10))
(assert (=> mode3U_{0} mode3L_{0}))
"""

cont_cond[3] = ["""
(assert (or (and mode3L_{0} mode3U_{0}     (and mode1U_{0} mode2U_{0})  (connect holder_{3} flow_12))
            (and mode3L_{0} mode3U_{0}     (xor mode1U_{0} mode2U_{0})  (connect holder_{3} flow_13))
            (and mode3L_{0} mode3U_{0} (not (or mode1U_{0} mode2U_{0})) (connect holder_{3} flow_14))
            (and mode3L_{0} (not mode3U_{0})                            (connect holder_{3} flow_15))
            (and (not mode3L_{0})                                       (connect holder_{3} flow_16))))
(assert (not (and (connect holder_{3} flow_12) (connect holder_{3} flow_13))))
(assert (not (and (connect holder_{3} flow_12) (connect holder_{3} flow_14))))
(assert (not (and (connect holder_{3} flow_12) (connect holder_{3} flow_15))))
(assert (not (and (connect holder_{3} flow_12) (connect holder_{3} flow_16))))
(assert (not (and (connect holder_{3} flow_13) (connect holder_{3} flow_14))))
(assert (not (and (connect holder_{3} flow_13) (connect holder_{3} flow_15))))
(assert (not (and (connect holder_{3} flow_13) (connect holder_{3} flow_16))))
(assert (not (and (connect holder_{3} flow_14) (connect holder_{3} flow_15))))
(assert (not (and (connect holder_{3} flow_14) (connect holder_{3} flow_16))))
(assert (not (and (connect holder_{3} flow_15) (connect holder_{3} flow_16))))"""]

jump_cond[3] = ["""
(assert (and (= d3_{1}_0 d3_{0}_t) (= g3_{1}_0 g3_{0}_t)))
(assert (or (and (<= g3_{0}_t (* (- 1 0.166) d3_{0}_t)) 
                 (= mode3L_{1} false) (= mode3U_{1} false))
            (and (>  g3_{0}_t (* (- 1 0.166) d3_{0}_t)) 
                 (= mode3U_{0} true)
                 (= mode3L_{1} true))))"""]

#############
# Init/Goal #
#############

init_cond = """
(assert (= tau_{0}_0 0))
(assert (and mode1U_{0} mode1L_{0}))
(assert (and (= g1_{0}_0 8.5) (= d1_{0}_0 0)))
(assert (and mode2U_{0} mode2L_{0}))
(assert (and (= g2_{0}_0 7.5) (= d2_{0}_0 0)))
(assert (and mode3U_{0} mode3L_{0}))
(assert (and (= g3_{0}_0 9.5) (= d3_{0}_0 0)))
"""

goal_cond = """
(assert (and (>= tau_{0}_t 0)))
"""

import sys
try:
    bound = int(sys.argv[1])
except:
    print("Usage:", sys.argv[0], "<Bound>")
else:
    generate(bound, 1, [0,1,2,3], 4, init_cond, goal_cond)
