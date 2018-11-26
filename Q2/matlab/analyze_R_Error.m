function solved_R_Error = analyze_R_Error(R_Error)

    R_Error = [
        zeros((36 - length(R_Error)), 1)
        R_Error
    ];

    X = (1 : 36)';

    lssvm_type = 'function estimation';
    lssvm_kernel = 'RBF_kernel';

    lssvm_model = initlssvm(X, R_Error, lssvm_type, [], [], lssvm_kernel);

    %optimize
    costfun = 'crossvalidatelssvm';
    costfun_args = {10, 'mse'};
    optfun = 'gridsearch';
    lssvm_model = tunelssvm(lssvm_model, optfun, costfun, costfun_args);

    lssvm_model = trainlssvm(lssvm_model);

    predict_X = (1 : 73)';
    solved_R_Error = simlssvm(lssvm_model, predict_X);
    return;
end