const CopyWebpackPlugin = require('copy-webpack-plugin');
const HTMLWebpackPlugin = require('html-webpack-plugin');
const path = require('path');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = {
	mode: 'development',
	devServer: {
		contentBase: 'dist',
		port: 3000,
		proxy: {
			'/api': {
				target: 'http://localhost:5000',
				pathRewrite: {"^/api": ""}
			},
			'/socket.io': {
				target: 'http://localhost:5000',
				ws: true
			}
		},
		headers: {
			"Access-Control-Allow-Origin": "*",
			"Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, PATCH, OPTIONS",
			"Access-Control-Allow-Headers": "X-Requested-With, content-type, Authorization"
		}
	},
	devtool: 'inline-source-map',

	plugins: [
		new CopyWebpackPlugin([{
			from: 'public/assets',
			to: 'assets'
		}]),
		new HTMLWebpackPlugin({
			template: 'public/index.html',
			filename: 'index.html'
		}),
		new MiniCssExtractPlugin({
			filename: 'css/mystyles.css'
		})
	],

	module: {
		rules: [{
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
		}]
	}
	// entry: [
		// 'webpack-dev-server/client?http://localhost:5000',
	// ],
};
