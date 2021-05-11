create or replace PROCEDURE MIKHEEV_OA_avg_ratings
IS 
BEGIN
  DELETE FROM avg_ratings;
  COMMIT;
INSERT INTO avg_ratings
    (ID_DRIVER, DRIVER_NAME, MONTH_DT, YEAR_DT, AVG_RAT )
SELECT  B.ID_DRIVER
        , B.DRIVER_NAME
        , B.MONTH_DT
        , B.YEAR_DT 
        , SUM(B.PROD_RATINGS) / SUM(B.CNT_RATINGS)
FROM    (SELECT  A.ID_DRIVER
                , A.DRIVER_NAME
                , A.MONTH_DT
                , A.YEAR_DT 
                , A.EVALUATION_TRIP 
                , COUNT(A.EVALUATION_TRIP) AS CNT_RATINGS
                , A.EVALUATION_TRIP * COUNT(A.EVALUATION_TRIP) AS PROD_RATINGS 
        FROM basic_showcase_one A
        GROUP BY A.ID_DRIVER
                , A.DRIVER_NAME
                , A.MONTH_DT
                , A.YEAR_DT 
                , A.EVALUATION_TRIP
        ORDER BY A.ID_DRIVER) B
GROUP BY B.ID_DRIVER
        , B.DRIVER_NAME
        , B.MONTH_DT
        , B.YEAR_DT;
    DBMS_OUTPUT.PUT_LINE('Выполнение процедуры завершено. Данные помещены в таблицу Avg_Ratings')  ;
    COMMIT;
END MIKHEEV_OA_avg_ratings;
