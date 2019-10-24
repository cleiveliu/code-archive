#lang racket
(struct event (name start end))
(define (make-event name start end)
  (if (and (string? name)
           (and (number? start) (number? end))
           (and (<= 0 start) (<= start 23))
           (and (<= 0 end) (<= end 23))
           (<= start end))
      (event name start end)
      "invalid params!"))
      
;;task 1
(define (event-time event)
  (- (event-end event) (event-start event)))
(define (total-duration lst)
  (cond
    [(null? lst) 0]
    [else
     (+ (event-time (car lst))
        (total-duration (cdr lst)))]))
;;test data tem
(define tlst1 (list
              (make-event "a" 1 2)
              (make-event "b" 2 3)
              (make-event "c" 1 3)
              (make-event "d" 5 10)))


;;task 2
;;return latest event between 2 events
(define (compare event1 event2)
  (if (> (event-end event1) (event-end event2))
      event1
      event2))
(define (latest-event lst)
  (cond
    [(null? (cdr lst)) (car lst)]
    [else
     (compare (car lst) (latest-event (cdr lst)))]))
;;task 3
(define (sort-by-start lst)
  (cond
    [(null? lst) lst]
    [else (append (sort-by-start (ealier-than (car lst) (cdr lst)))
                  (list (car lst))
                  (sort-by-start (later-than (car lst) (cdr lst))))]))

(define (ealier-than event1 lst)
  (filter (lambda (event2) (< (event-start event1) (event-start event2))) lst))
(define (later-than event1 lst)
  (filter (lambda (event2) (>= (event-start event2) (event-start event1))) lst))
;;task 4
(define (overlap? event1 event2)
  (not (or (<= (event-end event1) (event-start event2))
           (<= (event-end event2) (event-start event1)))))
(define (lists-event-overlap? event lst)
  (cond
    [(null? (cdr lst)) (overlap? (car lst) event)]
    [else
     (or (overlap? event (car lst))
         (lists-event-overlap? event (cdr lst)))]))
;;task 5
(define (lists-lists-overlap? lst1 lst2)
  (cond
    [(null? lst1) #f]
    [else
     (or (lists-event-overlap? (car lst1) lst2)
         (lists-lists-overlap? (cdr lst1) lst2))]))
;;task 6
; constants
(require 2htdp/image)
(require 2htdp/universe)
(require lang/posn)
(define width 300)
(define height 140)
(define hfwd (/ width 2))

(define tlst (list
              (make-event "breakfirst" 6 8)
              (make-event "take class" 8 12 )
              (make-event "havelanuch" 12 13)
              (make-event "read books" 21 22)
              (make-event "takeshower" 22 23)))
(define (event2text event)
  (string-append (event-name event)
                 "  from  "
                 (number->string (event-start event))
                 "  to  "
                 (number->string (event-end event))))
(define (eventlist2textlist lst)
  (cond
    [(null? lst) '()]
    [else
     (cons (text (event2text (car lst)) 20 "orange")
           (eventlist2textlist (cdr lst)))]))
(define (render ws)
  
  (place-images
   (eventlist2textlist tlst)
   (list (make-posn hfwd 20)
         (make-posn hfwd 40)
         (make-posn hfwd 60)
         (make-posn hfwd 80)
         (make-posn hfwd 100))
   (rectangle width height "solid" "white")))
(define (main frequency)
  (big-bang (make-posn 200 200) 
            [name "My events today"]
            [to-draw render] 
           
            
            
            ))
(main 1)
  

;;task 7
(define (rm-by-order order lst)
  (cond
    [(or (< order 1) (> order (length lst))) lst]
    [(= order 1) (cdr lst)]
    [else
     (cons (car lst)
           (rm-by-order (- order 1) (cdr lst)))]))
     


    



