create or replace PROCEDURE MIKHEEV_OA_disp_earnings
IS
BEGIN
  DELETE FROM disp_earnings ;
  COMMIT;
INSERT INTO disp_earnings
    (   ID_DISPATCHER, CNT_ORDERS, DISPATCHER_NAME, INCOME_DISP )
    SELECT  A.ID_DISPATCHER
            , COUNT(A.ID_DISPATCHER)
            , A.DISPATCHER_NAME
            , (SUM(A.FUEL_RATE) / 100) * A.PERC_DISPATHER AS INCOME_DISP
    FROM basic_showcase_one A 
    GROUP BY A.ID_DISPATCHER, A.DISPATCHER_NAME, A.PERC_DISPATHER ;
    DBMS_OUTPUT.PUT_LINE('Выполнение процедуры завершено. Данные помещены в таблицу disp_earnings')  ;
    COMMIT;
END MIKHEEV_OA_disp_earnings;