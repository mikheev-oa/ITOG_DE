create or replace PROCEDURE MIKHEEV_OA_compl_app
IS
BEGIN
    DELETE FROM compl_app;
    COMMIT;
    INSERT INTO compl_app
            (MONTH_YEAR_DT, CNT_MONTH_DT, CNT_YEAR_DT)
    SELECT  CASE
                WHEN MONTH_DT = 1 THEN '������ ' || YEAR_DT || ' �.'
                WHEN MONTH_DT = 2 THEN '������� ' || YEAR_DT || ' �.'
                WHEN MONTH_DT = 3 THEN '���� ' || YEAR_DT || ' �.'
                WHEN MONTH_DT = 4 THEN '������ ' || YEAR_DT || ' �.'
                WHEN MONTH_DT = 5 THEN '��� ' || YEAR_DT || ' �.'
                WHEN MONTH_DT = 6 THEN '���� ' || YEAR_DT || ' �.'
                WHEN MONTH_DT = 7 THEN '���� ' || YEAR_DT || ' �.'
                WHEN MONTH_DT = 8 THEN '������ ' || YEAR_DT || ' �.'
                WHEN MONTH_DT = 9 THEN '�������� ' || YEAR_DT || ' �.'
                WHEN MONTH_DT = 10 THEN '������� ' || YEAR_DT || ' �.'
                WHEN MONTH_DT = 11 THEN '������ ' || YEAR_DT || ' �.'
                WHEN MONTH_DT = 12 THEN '������� ' || YEAR_DT || ' �.'
              END AS MONTH_YEAR_DT
              , COUNT(MONTH_DT) AS CNT_MONTH_DT
              , COUNT(YEAR_DT) AS CNT_YEAR_DT
    FROM basic_showcase_one
    GROUP BY MONTH_DT, YEAR_DT
    ORDER BY YEAR_DT ASC ;
    DBMS_OUTPUT.PUT_LINE('���������� ��������� ���������. ������ �������� � ������� COMPL_APP')  ;
    COMMIT;
END MIKHEEV_OA_compl_app;