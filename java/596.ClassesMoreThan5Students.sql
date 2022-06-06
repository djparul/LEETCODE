# https://leetcode.com/problems/classes-more-than-5-students/
select class from 
    (select class, count(student) from 
     
        ( select distinct class, student
          from Courses
        )   
     having count(student) >=5 
     group by class );