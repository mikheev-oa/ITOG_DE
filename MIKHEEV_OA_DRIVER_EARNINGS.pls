create or replace PROCEDURE MIKHEEV_OA_driver_earnings
IS
BEGIN
  DELETE FROM driver_earnings ;
  COMMIT;
INSERT INTO driver_earnings
    (   ID_DRIVER, CNT_ORDERS, DRIVER_NAME, INCOME_DRIVER )
    SELECT  A.ID_DRIVER
            , COUNT(A.ID_DRIVER)
            , A.DRIVER_NAME
            , (SUM(A.FUEL_RATE) / 100) * A.PERC_DRIVER AS INCOME_DRIVER
    FROM basic_showcase_one A 
    GROUP BY A.ID_DRIVER, A.DRIVER_NAME, A.PERC_DRIVER ;
    DBMS_OUTPUT.PUT_LINE('Выполнение процедуры завершено. Данные помещены в таблицу driver_earnings')  ;
    COMMIT;
END MIKHEEV_OA_driver_earnings;