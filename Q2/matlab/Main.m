load('data.mat');
load('R_Error.mat');

sectors = {
    'Banking',
    'Beauty and personal care',
    'Communications technology',
    'Computer hardware',
    'Computer software',
    'Construction/infrastructure/gardening',
    'Electronics/appliances/semiconductor/instrumentation',
    'Engineering/machinery/energy',
    'Fashion/textile/furs',
    'General merchandise/chains/retail',
    'Hotels/tourism',
    'HR',
    'Insurance',
    'Internet development and application',
    'Legal profession/law',
    'Other',
    'Real property',
    'Restaurants & recreation',
    'Sales',
    'Science & Technology',
    'Securities/finance/investment',
    'Security/housekeeping/other',
    'Technical work'
};

origin_raw_hash = containers.Map(sectors, {
    49, 43, 9, 5, 1, 24, 10, 12, 48, 44, 42, 13, 28, 6, 18, 47, 39, 41, 4, 17, 27, 45, 31
});

ARIMA_predicts_hash = containers.Map(sectors, {
    banking,
    beautyand,
    Communication,
    computerhf,
    computersf,
    Construction,
    ElectronicApplicance,
    Engineering,
    fashion,
    generalme,
    Hotel,
    HR,
    Insurance,
    Internetdevelopment,
    Law,
    other,
    RealProperty,
    restaurant,
    Sales,
    sciencetech,
    Security,
    securityhousekeeping,
    Technicalwork
});

R_error_hash = containers.Map(sectors, {
    banking_RE,
    beautyand_RE,
    Communication_RE,
    computerhf_RE,
    computersf_RE,
    Construction_RE,
    ElectronicApplicance_RE,
    Engineering_RE,
    fashion_RE,
    generalme_RE,
    Hotel_RE,
    HR_RE,
    Insurance_RE,
    Internetdevelopment_RE,
    Law_RE,
    other_RE,
    RealProperty_RE,
    restaurant_RE,
    Sales_RE,
    sciencetech_RE,
    Security_RE,
    securityhousekeeping_RE,
    Technicalwork_RE
});

MAPES = containers.Map({'default'}, {containers.Map({'default1', 'default2', 'default3'}, {1.0, 1.0, 1.0})});
sectors = sectors';
for sector = sectors
    sector = sector{1};
    MAPES(sector) = train_and_plot(ARIMA_predicts_hash(sector), origin_raw_hash(sector), R_error_hash(sector), data, sector);
end

models = {'LSSVM', 'ARIMA', 'ARIMA-LSSVM'};
for sector = sectors
    sector = sector{1};

    fprintf('%s :\n', sector);

    for model = models
        model = model{1};
        temp = MAPES(sector);

        fprintf('\t%s : %s\n', model, num2str(temp(model)));
    end
end