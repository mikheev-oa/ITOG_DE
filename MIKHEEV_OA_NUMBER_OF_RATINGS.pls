create or replace PROCEDURE MIKHEEV_OA_number_of_ratings
IS
BEGIN
  DELETE FROM number_of_ratings;
  COMMIT;
INSERT INTO number_of_ratings
    (MONTH_DT, YEAR_DT, EVAL_TRIP )
SELECT B.MONTH_DT
        , B.YEAR_DT
        , SUM(EVAL_TRIP)
FROM (  SELECT  A.MONTH_DT
                ,  A.YEAR_DT
                ,  A.EVALUATION_TRIP  
                , COUNT( A.EVALUATION_TRIP) AS EVAL_TRIP
        FROM basic_showcase_one A 
        GROUP BY  A.EVALUATION_TRIP,  A.MONTH_DT,  A.YEAR_DT
        ORDER BY  A.YEAR_DT ASC) B
GROUP BY B.MONTH_DT, B.YEAR_DT
ORDER BY B.YEAR_DT;
    DBMS_OUTPUT.PUT_LINE('Выполнение процедуры завершено. Данные помещены в таблицу NUMBER_OF_RATINGS')  ;
    COMMIT;
END MIKHEEV_OA_number_of_ratings;