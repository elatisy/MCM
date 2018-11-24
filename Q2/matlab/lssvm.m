load('data.mat'); % value: data

% Xtrain = (1 : 30)';
% Ytrain = (data(1, 1 : 30))';

% Xtest = (31 : 36)';
% Ytest = (data(1, 31 : 36))';

% Xpredict = (43 : 48)';

Xpredict = (2 : 36)';

Xorigin = (1 : 36)';
Yorigin = (data(1, 1 : 36))';

gam = 100000;
sig2 = 0.1;
lssvm_type = 'function estimation';
lssvm_kernel = 'RBF_kernel';

% % lssvm_model = initlssvm(Xorigin, Yorigin, lssvm_type, gam, sig2, lssvm_kernel);

% % %optimize
% % costfun = 'crossvalidatelssvm';
% % costfun_args = {10, 'mse'};
% % optfun = 'gridsearch';
% % lssvm_model = tunelssvm(lssvm_model, optfun, costfun, costfun_args);

% % %train
% % lssvm_model = trainlssvm(lssvm_model);

% % %predict
% % Ypredict = simlssvm(lssvm_model, Xpredict);

% % figure;
% % plot(Xpredict, Ypredict, 'r-x');
% % hold on;
% % plot(Xorigin, Yorigin, 'r-o');

residual_error = [    
    -96.31775562141089
    24.07943890535272
    23.11626134913861
    -192.6355112428218
    293.3851466001724
    209.1281137233541
    -144.6463219715894
    -74.58615272508351
    -58.11960940388369
    224.5910393457851
    -200.8734230393593
    -162.5167730895107
    32.85331492206311
    -126.0937469201015
    1.585629024171666
    19.90710243749806
    643.4565657858742
    -555.3474049952928
    -117.4277346285605
    19.99334079295613
    58.35674285348544
    173.8020856423354
    -21.52382311557729
    -159.9235072626429
    267.4152455056872
    -102.0794672162671
    56.25359944518571
    -220.3945749232774
    -84.90310555815892
    194.0249921306699
    -96.95368019055362
    70.44029322275655
    -138.3961196299605
    101.9175999416402
    5.065203622044045
    ];

arima_predict = [
    0
    0
    0
    0
    0
    0
    0
    0
    0
    309.1517898726855
    262.4203157431718
    490.44085279481
    244.4030044450929
    117.1036682924127
    195.2588489099636
    45.41229481810071
    -4.933167982420777
    56.7155907489181
    785.0618910143824
    163.5788120872662
    -7.019063362905981
    16.60582410971787
    101.0864286998114
    232.5376296103077
    174.0260904816386
    153.5717867904695
    305.0844173315712
    167.7436726624073
    221.4052624649352
    136.9071520378326
    -16.03423935645367
    142.9583010002825
    11.55634959480756
    172.3994134080419
    163.4793878640243
    163.4140636919482
    89.24201650503015
    150.6962978542108
    155.5305181672281
    140.6971354994458
    105.2265155296384
    106.4482438550744
    142.1037394064556
    123.4071129738917
    122.5546078516312
    134.50794107014
    135.4482343252974
    132.5630266246623
    125.6637165903118
    125.9013522026046
    132.8366219680267
    129.1999834636958
    129.0341646212467
    131.3591804199158
    131.542074733465
    130.9808795116977
    129.6389103273247
    129.6851322925964
    131.0340959228976
    130.326741595694
    130.2944885478317
    130.7467221102401
    130.7822964693511
    130.6731396565278
    130.4121162668206
    130.4211067967036
    130.6834906602626
    130.5459047705412
    130.5396313031774
    130.6275942301758
    130.6345137182758
    130.6132818735922
    130.5625108046529

];

X = (1 : length(residual_error))';

lssvm_model = initlssvm(X, residual_error, lssvm_type, gam, sig2, lssvm_kernel);

%optimize
costfun = 'crossvalidatelssvm';
costfun_args = {10, 'mse'};
optfun = 'gridsearch';
lssvm_model = tunelssvm(lssvm_model, optfun, costfun, costfun_args);

%train
lssvm_model = trainlssvm(lssvm_model);

%predict
Ypredict = simlssvm(lssvm_model, Xpredict);
Ypredict = [
    Ypredict
    zeros((length(arima_predict) - length(Ypredict) - 1), 1)
];

arima_fixed = [
    0
    Ypredict
] + arima_predict;
X = [
    X
    36
];

arima_predict_x = (1 : length(arima_predict))';
% length(arima_predict_x)
% length(arima_fixed)
[alpha, b] = trainlssvm({arima_predict_x, arima_fixed, lssvm_type, gam, sig2, lssvm_kernel});

Xpredict = (1 : 80)';
Ypredict = simlssvm({arima_predict_x, arima_fixed, lssvm_type, gam, sig2, lssvm_kernel}, {alpha, b}, Xpredict);

figure;
plot(Xpredict, Ypredict, 'r-*');
hold on;
% figure;
% plot(X, Ypredict, '-');

% figure;
plot(Xorigin, Yorigin, 'r-o');
% hold on;
% X = [
%     X
%     36
% ];
plot(arima_predict_x, arima_fixed, 'r-x');
% hold on;

% plot(X, arima_predict, '-');