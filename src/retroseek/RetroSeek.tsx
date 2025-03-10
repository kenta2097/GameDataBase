import React, { useState } from 'react';
import { SearchForm } from './components/SearchForm';
import { GameList } from './components/GameList';
import { GameService } from './services/GameService';
import { Game } from './models/Game';
import './styles/RetroSeek.css';

const gameService = new GameService();

export const RetroSeek: React.FC = () => {
    const [games, setGames] = useState<Game[]>([]);

    const handleSearch = async (criteria: any) => {
        const results = await gameService.searchGames(criteria);
        setGames(results);
    };

    return (
        <div className="retroseek">
            <h1>RetroSeek</h1>
            <SearchForm onSearch={handleSearch} />
        </div>
    );
};

export default RetroSeek;
