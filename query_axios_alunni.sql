# ottieni anno scolastico

SELECT ANS.iAnsID, ANS.dAnsInizio, ANS.dAnsFine,ANS.iAnsValore,
 ANS.dAnsAxiosInizio, ANS.dAnsAxiosFine, ANS.sAnsNote FROM TAns_AnniScolast ANS
 WHERE  ANS.iAnsValore LIKE '2013'
 
 
 #ottieni tipolo alunno
 
 SELECT CAG.iCagId, CAG.sCagLDescAxios FROM TCAG_ANACATEG CAG WHERE (CAG.dDelete IS NULL) AND (CAG.dEnd IS NULL) AND (CAG.iCagID IN ( 0,1 ))
 
 #ottieni cose per i recuperi
 
 SELECT TFre.sFreSDesc, afd.iAnsFreDwgId FROM
        TAnsFreDwg afd INNER JOIN TFre_FasiRec TFre
         ON (TFre.iFreId = afd.iFreId) WHERE (afd.iAnsId = 44) 
           AND (afd.iDwgId IS NULL) ORDER BY afd.iAnsFreDwgId
           
           
 #ottieni lista di tutti gli alunni indipendentemente dal anno scolastico
 
 SELECT DISTINCT ana.IANAID, ana.SANACOGNOME, ana.SANANOME, ana.DANANASCITA,
                ana.SANACODFISCALE, ana.IIOCTRLCODE, ana.SANACOGNOMENOMEIDX, ana.ISRPCID, 
                ana.ISRPCID AS iSrpcIDCom, ana.ISRPCID AS iSrpcIDSta, srpc.ICOMID, srpc.istaid, 
                anacag.IANACAGID, anacag.SANACAGCODE, cag.ICAGID, cag.SCAGLDESCAXIOS, sex.SSEXSDESC, 
                anastc.IANASTCID, anastc.ISTCSEXID, ana.IVOMID, vom.SVOMDESC,
                 NULL AS IDWGSEDID, NULL AS IDWGID, NULL AS SCLSDESC, ANA.ISEXID, 
                 ANA.LANACONSPRIVACY, ANA.LANACODFISFITT, 
                 ANA.SANAPWPERT, 'kqb_ANA_ALU_Select' AS qid, 0 AS TheEnd 
                 FROM TANA_ANAGRAFICHE ana INNER JOIN TANACAG anacag ON ( ana.IANAID = anacag.IANAID )
                 INNER JOIN TCAG_ANACATEG cag ON ( cag.ICAGID = anacag.ICAGID )
                  LEFT JOIN TVOM_VIVOMORTO vom ON ( vom.IVOMID = ana.IVOMID ) 
                  LEFT JOIN TSIT_SITUAZIONI sit ON ( ana.IANAID = sit.IANAID ) 
                  LEFT JOIN TCLSPST clspst ON ( clspst.ICLSPSTID = sit.ICLSPSTID) 
                  LEFT JOIN VCLS_CLASSI cls ON ( cls.ICLSID = clspst.ICLSID) 
                  LEFT JOIN TANASTC anastc ON ( ana.IANAID = anastc.IANAID ) 
                  LEFT JOIN TSTCSEX stcsex ON ( 
stcsex.ISTCSEXID = anastc.ISTCSEXID ) 
LEFT JOIN TSTCNEW stcnew ON ( stcnew.ISTCNEWID = stcsex.ISTCNEWID ) 
LEFT JOIN TSEX_SESSO sex ON ( sex.ISEXID = stcsex.ISEXID ) 
LEFT JOIN TSRPC srpc ON ( ana.ISRPCID = srpc.ISRPCID) WHERE (ana.DDELETE IS NULL) AND (CAG.iCagId = 1 ) ORDER BY ANA.sAnaCognomeNomeIdx 


#ottieni luoghi di nascita

SELECT  srpc.isrpcid, com.scomdesc, pro.sprosigla, srpc.ssrpccodcata, stacom.scomstadesc sComProv,nullcom.scomstadesc sComune,
        srpc.istaid    FROM    tsrpc srpc inner JOIN tpro_province pro ON pro.iproid = srpc.iproid  inner join tsta_stati sta on sta.istaid = srpc.istaid       
               left JOIN tcom_comuni com  ON com.icomid = srpc.icomid,            paxl_comsta(sta.sstaldesc, pro.sprosigla, com.scomdesc) stacom,   
                paxl_comsta(sta.sstaldesc, null, com.scomdesc) nullcom      
                     WHERE (tsrpc.ddelete IS NULL)                             ORDER BY 2 
                     
#ottieni id viventi
SELECT    iVomID, sVomDesc FROM  TVom_VivoMorto 
risultato(1)




#alunni anno scolastico


SELECT DISTINCT ana.IANAID, ana.SANACOGNOME, ana.SANANOME, ana.DANANASCITA, ana.SANACODFISCALE, ana.IIOCTRLCODE, ana.SANACOGNOMENOMEIDX, ana.ISRPCID, ana.ISRPCID AS iSrpcIDCom, ana.ISRPCID AS iSrpcIDSta, srpc.ICOMID, srpc.istaid, anacag.IANACAGID, anacag.SANACAGCODE, cag.ICAGID, cag.SCAGLDESCAXIOS, sex.SSEXSDESC, anastc.IANASTCID, anastc.ISTCSEXID, ana.IVOMID, vom.SVOMDESC, cls.IDWGSEDID, cls.IDWGID, cls.SCLSDESC AS SCLSDESC, ANA.ISEXID, ANA.LANACONSPRIVACY, ANA.SANAPWPERT, sed.SSEDMECCOD, ANA.LANACODFISFITT, ANA.SANACODALUSIDI, ANA.SANASTATOSOGEI AS stato_sogei, pa.ISTAATTID, 'kqb_ANA_ALU_Select' AS qid, 0 AS TheEnd FROM TANA_ANAGRAFICHE ana INNER JOIN TANACAG anacag ON ( ana.IANAID = anacag.IANAID ) INNER JOIN TCAG_ANACATEG cag ON ( cag.ICAGID = anacag.ICAGID ) LEFT JOIN TVOM_VIVOMORTO vom ON ( vom.IVOMID = ana.IVOMID ) LEFT JOIN TSIT_SITUAZIONI sit ON ( ana.IANAID = sit.IANAID ) LEFT JOIN TCLSPST clspst ON ( clspst.ICLSPSTID = sit.ICLSPSTID) LEFT JOIN VCLS_CLASSI cls ON ( cls.ICLSID = clspst.ICLSID) LEFT 
JOIN TANASTC anastc ON ( ana.IANAID = anastc.IANAID ) LEFT JOIN TSTCSEX stcsex ON ( stcsex.ISTCSEXID = anastc.ISTCSEXID ) LEFT JOIN TSTCNEW stcnew ON ( stcnew.ISTCNEWID = stcsex.ISTCNEWID ) LEFT JOIN TSEX_SESSO sex ON ( sex.ISEXID = stcsex.ISEXID ) LEFT JOIN TSRPC srpc ON ( ana.ISRPCID = srpc.ISRPCID) LEFT JOIN VSED_SEDI sed ON (sed.IDWGSEDID = cls.IDWGSEDID) LEFT JOIN VPOSATT pa ON ( pa.IPOSATTID = sit.IPOSATTID) WHERE (ana.DDELETE IS NULL) AND (CAG.iCagId = 1 ) AND ((SIT.isitordine = 1) AND (SIT.dstart='2013-09-01') AND (CLS.idwgid=102)) ORDER BY ANA.sAnaCognomeNomeIdx
                     