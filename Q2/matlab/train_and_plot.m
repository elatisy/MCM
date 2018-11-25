function [] = train_and_plot(arima_predict, data, origin_raw, plot_title)
    arima_predict = [
        zeros(73 - length(arima_predict), 1)
        arima_predict
    ];

    Yorigin = (data(origin_raw, 1:36));

    Xorigin = [];
    Y_temp = [];
    i = 1;
    
    for y = Yorigin(1:36)
        if ~isnan(y)
            Xorigin = [
                Xorigin
                i
            ];
            Y_temp = [
                Y_temp
                y
            ];
        end
    
        i = i + 1;
    end
    Yorigin = Y_temp;

    lssvm_type = 'function estimation';
    lssvm_kernel = 'RBF_kernel';

    gam = 10;
    sig2 = 0.003;
    lssvm_model = initlssvm(Xorigin(1 : length(Xorigin) - 3), Yorigin(1 : length(Yorigin) - 3), lssvm_type, gam, sig2, lssvm_kernel);

    %optimize
    costfun = 'crossvalidatelssvm';
    costfun_args = {10, 'mse'};
    optfun = 'gridsearch';
    lssvm_model = tunelssvm(lssvm_model, optfun, costfun, costfun_args);

    lssvm_model = trainlssvm(lssvm_model);

    %LSSVM predict
    Xpredict = (1:80)';
    Ypredict = simlssvm(lssvm_model, Xpredict);

    arima_fixed = (arima_predict + Ypredict(1 : length(arima_predict))) ./ 2;

    figure;
    arima_predict_x = (1:length(arima_predict));
    plot(Xorigin, Yorigin, 'r-+', Xpredict, Ypredict, 'g-*', arima_predict_x, arima_predict, 'k-x', arima_predict_x, arima_fixed, 'b-o');
    legend('Original', 'LSSVM', 'ARIMA', 'ARIMA-LSSVM');
    title(plot_title)
    xlabel('sequence');
    ylabel('demand/person');

    len = 5;
    YO_length = length(Yorigin);
    YO_verify = Yorigin((YO_length - 4));

    % Ypredict_MAPE = sum(abs(YO_verify - Ypredict(32:36)) ./ YO_verify) * 100 / len;
    % arima_predict_MAPE = sum(abs((YO_verify - arima_predict(32:36)) ./ YO_verify)) * 100 / len;
    % arima_fixed_MAPE = sum(abs((YO_verify - arima_fixed(32:36)) ./ YO_verify)) * 100 / len;

    % if strcmp(plot_title, 'Computer hardware')
    %     plot(Xorigin, Yorigin, 'r-*', arima_predict_x, arima_predict, 'b-o');
    %     legend('Original', 'ARIMA');
    %     title(plot_title);
    %     xlabel('sequence');
    %     ylabel('demand/person');
    % end

    % text(60, 500, strcat('LSSMA_MAPE: ' , num2str(Ypredict_MAPE), 'ARIMA_MAPE: ', num2str(arima_predict_MAPE), 'ARIMA-LSSVM_MAPE: ', num2str(arima_fixed_MAPE)));
end
