const CopyWebpackPlugin = require('copy-webpack-plugin');
const HTMLWebpackPlugin = require('html-webpack-plugin');
const TerserPlugin = require('terser-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = {
    mode: 'production',
    module: {
        rules: [{
            test: /\.(js)$/,
            exclude: /node_modules/,
            use: {
                loader: 'babel-loader'
            }
        },
            {
                test: /\.scss$/,
                use: [
                    MiniCssExtractPlugin.loader,
                    {
                        loader: 'css-loader'
                    },
                    {
                        loader: 'sass-loader',
                        options: {
                            sourceMap: true,
                            // options...
                        }
                    }
                ]
            }
    ]},
    optimization: {
        minimizer: [new TerserPlugin()]
    },
    plugins: [
        new CopyWebpackPlugin([{
            from: 'public/assets',
            to: 'assets'
        }]),
        new HTMLWebpackPlugin({
            template: 'public/index.html',
            filename: 'index.html',
            hash: true,
            minify: false
        }),
        new MiniCssExtractPlugin({
			filename: 'css/mystyles.css'
		})
    ]
};
